from django.contrib import admin
from .models import users
from .models import fileUploads

# Register your models here.
admin.site.register(users)
admin.site.register(fileUploads)