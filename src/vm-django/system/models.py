from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


class Course(models.Model):
    """
    Course Model, practicals refer to a specific course they belong to 
    """

    name = models.TextField()
    instructor_name = models.TextField()



class Practical(models.Model):
    """
    Practical model, Groups refer to a specific practical that they belong to.
    """
    # to be implemented

    name = models.TextField()
    ta_name = models.TextField()

    course = models.ForeignKey(Practical, null=True, related_name='practical',
                                  on_delete=models.CASCADE)



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


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_ta = models.BooleanField(default=False)

    group = models.ForeignKey(Group, null=True, related_name='profile',
                              on_delete=models.CASCADE)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.name
