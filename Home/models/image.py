from django.db import models

class Image(models.Model):

    images = models.ImageField(upload_to='uploads/images/' , default='')

