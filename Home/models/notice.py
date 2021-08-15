from django.db import models

class Notice(models.Model):

    name = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='uploads/notices/', default='')

    @staticmethod
    def getNotice():
        return Notice.objects.all()