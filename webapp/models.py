from django.db import models

# Create your models here.
class FF(models.Model):
    fil = models.FileField(upload_to='files')
