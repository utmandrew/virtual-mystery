from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


class Practical(models.Model):
    """
    Practical model, Groups refer to a specific practical that they belong to.
    """
    name = models.TextField(null=True)
    pass


class Group(models.Model):
    """
    Group model, Users refer to a specific group that they belong to.
    """
    # group name
    name = models.TextField(null=True)

    # refers to a groups practical
    # remove null=True when in production (used for admin accounts)
    practical = models.ForeignKey(Practical, null=True, related_name='group',
                                  on_delete=models.CASCADE)


class User(AbstractUser):
    """
    Custom user model.
    """
    # refers to a users group
    # remove null=True when in production (used for admin accounts)

    is_ta = models.BooleanField(default=False)
    
    group = models.ForeignKey(Group, null=True, related_name='profile',
                              on_delete=models.CASCADE)
