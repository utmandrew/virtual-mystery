from django.contrib import admin
from .models import Mystery, Instance, Release

# Register your models here.
admin.site.register(Mystery)
admin.site.register(Instance)
admin.site.register(Release)
