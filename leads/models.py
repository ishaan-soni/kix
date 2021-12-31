from django.db import models
# from django.contrib.auth import get_user_model -> built in user model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser): # has all fields from abstractuser class
    pass # to add custom fields remove pass || configure in settings.py file as own user model.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #getting details from actual User model. 
    def __str__(self):
        return self.user.username


class Lead(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) #assigning an agent to every lead || on_delete refers to what happens when agent is deleted
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    # phoned = models.BooleanField(default=False)
    # sources = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    # profile_picture = models.ImageField(blank = True,null = True)
    # files = models.FileField(blank=True,null=True)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #creates one agent for one user
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.email



def post_user_created_signal(sender, instance, created, **kwargs): 
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User) #User is sending a signal once user is saved
    
    
