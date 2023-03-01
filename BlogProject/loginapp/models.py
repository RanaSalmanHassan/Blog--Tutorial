from django.db import models
from django.contrib.auth.models import User
# To automatically create one to one object
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics')
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    phone_number = models.CharField(max_length=11,blank=True)
    website = models.URLField(blank=True)

@receiver(post_save,sender= User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save,sender= User)
def save_profile(sender,instance,**kwargs):
    instance.user_profile.save()