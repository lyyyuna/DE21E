import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from draceditor.utils import LazyEncoder
from qcloud_cos import CosClient
from qcloud_cos import UploadFileRequest


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image._size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            try:
                img_uuid = "{0}".format(uuid.uuid4().hex[:10])
                tmp_file = os.path.join(settings.DRACEDITOR_UPLOAD_PATH, img_uuid)
                def_path = default_storage.save(tmp_file, ContentFile(image.read()))
                # img_url = os.path.join(settings.MEDIA_URL, def_path)
                cos_client = CosClient(
                            settings.APPID, 
                            settings.SECRET_ID, 
                            settings.SECRET_KEY, 
                            region=settings.REGION_INFO)
                request = UploadFileRequest(settings.BUCKET, '/'+def_path, def_path)
                upload_file_ret = cos_client.upload_file(request)
                img_url = settings.IMAGEFQDN + def_path
                data = json.dumps({
                    'status': 200,
                    'link': img_url,
                    'name': u'image'
                })
            except:
                data = json.dumps({
                    'status': 405,
                    'error': _('Some thing wrong.')
                }, cls=LazyEncoder)


            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))