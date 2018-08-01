from django.db import models
import hashlib

# Create your models here.


class Mystery(models.Model):
    """
    Mystery template.
    """
    # mystery name
    name = models.TextField()
    # hashed mystery name
    hash = models.CharField(max_length=64, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        """
        overriding the default save method.
        """
        # automatically fills in mystery hash value
        if self.hash is None:
            self.hash = hashlib.sha256(bytes(self.name, 'utf-8')).hexdigest()
        # calling the default save function
        super().save(*args, **kwargs)


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


class Release(models.Model):
    """
    Mystery release.
    """
    # release mystery
    mystery = models.ForeignKey(Mystery, related_name='release',
                                on_delete=models.CASCADE)
    # release number
    number = models.PositiveIntegerField()
    # release number (hashed)
    hash = models.CharField(max_length=64, blank=True, null=True, default=None)
    # clue.txt
    clue = models.TextField()
    # ans.txt
    answer = models.TextField()

    def save(self, *args, **kwargs):
        """
        overriding the default save method.
        """
        # automatically fills in release hash value
        if self.hash is None:
            self.hash = hashlib.sha256(bytes(str(self.number), 'utf-8'))\
                .hexdigest()
        # calling the default save method
        super().save(*args, **kwargs)
