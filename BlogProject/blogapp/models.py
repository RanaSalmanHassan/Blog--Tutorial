from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog_Model(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_author')
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='blog_pics')
    description = models.TextField()
    category = models.CharField(max_length=60)
    date_added = models.DateTimeField(auto_now_add=True)