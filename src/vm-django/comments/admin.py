from django.contrib import admin
from .models import Comment, Reply, Result

# Register your models here.
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Result)
