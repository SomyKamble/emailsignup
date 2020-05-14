from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(max_length=200,blank=True)
    #location= models.CharField(max_length=200,blank=True)
    birth_date=models.CharField(max_length=500,null=True,blank=True)
    email_confirmed=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

#post_save.connect(update_user_profile,sender=User)

class prof(User):
    req=models.CharField(max_length=200)

    def __str__(self):
        return self.req



class Posm(models.Model):
    title=models.CharField(max_length=500)

    def __str__(self):
        return self.title

def save_pos(sender,instance,**kwargs):
    print("this has been executed")
    print(instance)

pre_save.connect(save_pos,sender=Posm)
post_save.connect(save_pos,sender=Posm)