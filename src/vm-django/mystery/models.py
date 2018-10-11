from django.db import models
import hashlib
import hmac
from django.conf import settings

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
            # self.hash = hashlib.sha256(bytes(self.name, 'utf-8')).hexdigest()
            # hash based off of secret key
            self.hash = hmac.new(bytes(settings.SECRET_KEY, 'utf-8'),
                                 msg=bytes(self.name, 'utf-8'),
                                 digestmod=hashlib.sha256).hexdigest()
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
    # clue.txt
    clue = models.TextField()
    # ans.txt
    answer = models.TextField()

    class Meta:
        ordering = ('number',)

    @property
    def hash(self):
        """
        Returns a 64 hex-character sha256 hash of the release id (unique)
        based off of the secret key, set in the settings file.
        """
        # return hashlib.sha256(bytes(str(self.id), 'utf-8')).hexdigest()
        # hash based off of secret key
        return hmac.new(bytes(settings.SECRET_KEY, 'utf-8'),
                        msg=bytes(str(self.id), 'utf-8'),
                        digestmod=hashlib.sha256).hexdigest()

    # def save(self, *args, **kwargs):
    #     """
    #     overriding the default save method.
    #     """
    #     # automatically fills in release hash value
    #     if self.hash is None:
    #         self.hash = hashlib.sha256(bytes(str(self.number), 'utf-8'))\
    #             .hexdigest()
    #     # calling the default save method
    #     super().save(*args, **kwargs)
