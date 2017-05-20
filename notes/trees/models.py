from django.db import models


class OFile(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    ofile = models.FileField(upload_to="staticfile/%Y/%m/")
    createtime = models.DateTimeField(auto_now=True)

    def get_url(self):
        return self.ofile.url


class OImage(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    oimage = models.FileField(upload_to="image/%Y/%m/")
    createtime = models.DateTimeField(auto_now=True)

    def get_url(self):
        return self.oimage.url