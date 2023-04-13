from django.contrib import admin
from .models import Blog_Model,Comment
# Register your models here.
admin.site.register(Blog_Model)
admin.site.register(Comment)