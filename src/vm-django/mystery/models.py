from django.db import models

# Create your models here.


class Mystery(models.Model):
    """
    Mystery template.
    """
    # mystery name
    name = models.TextField()


class Instance(models.Model):
    """
    Mystery instance.
    """
    # refers to a mystery template
    mystery = models.ForeignKey(Mystery, related_name='instance',
                                on_delete=models.CASCADE)
    # refers to a group
    group = models.ForeignKey('system.Group', related_name='instance',
                              on_delete=models.CASCADE)
