from django.contrib import admin
from .models import Blog_Model,Comment,Like
# Register your models here.
admin.site.register(Blog_Model)
admin.site.register(Comment)
admin.site.register(Like)
