from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username +' - '+ self.email

class fileUploads(models.Model):
    file_name = models.FileField()
    file_uploader = models.CharField(max_length=200)

