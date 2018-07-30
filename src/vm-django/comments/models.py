from django.db import models
from django.conf import settings

# Create your models here.


class Comment(models.Model):
    """
    A comment model.
    """
    # datetime created
    created = models.DateTimeField(auto_now_add=True)
    # comment owner
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment',
                              on_delete=models.CASCADE)
    # mystery instance
    instance = models.ForeignKey('mystery.Instance', related_name='comment',
                                 on_delete=models.CASCADE)
    # mystery release (clue/week)
    release = models.PositiveIntegerField()
    # comment text (no max char count)
    text = models.TextField()

    class Meta:
        ordering = ('created',)


class Reply(models.Model):
    """
    A comment reply model.
    """
    # datetime created
    created = models.DateTimeField(auto_now_add=True)
    # reply owner
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reply',
                              on_delete=models.CASCADE)
    # reply text (no max char count)
    text = models.TextField()
    # refers to parent comment
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE,
                               related_name='reply')

    class Meta:
        ordering = ('created',)
