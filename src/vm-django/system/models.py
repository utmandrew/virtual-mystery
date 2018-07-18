from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Practical(models.Model):
    """
    Practical model, Groups refer to a specific practical that they belong to.
    """
    # to be implemented
    pass


class Group(models.Model):
    """
    Group model, Users refer to a specific group that they belong to.
    """
    # group name
    name = models.TextField()
    # refers to a groups practical
    # remove null=True when in production (used for admin accounts)
    practical = models.ForeignKey(Practical, null=True, related_name='group',
                                  on_delete=models.CASCADE)


class Profile(models.Model):
    """
    Extension of default django user model. (no inheritance)
    User profile info.
    """
    # link to the default django user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # refers to a users group
    # remove null=True when in production (used for admin accounts)
    group = models.ForeignKey(Group, null=True, related_name='profile',
                                 on_delete=models.CASCADE)


# Delete depending on whether a user should have their profile info filled out
# on signup or not
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a Profile object for each user.
    """
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)