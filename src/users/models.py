import os

from django.db import models
from django.contrib.auth.models import User

from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass

    def __call__(self, instance, filename):
        print(f"\n\nFilename = {filename}\n\n")
        print(f"\n\nInstance = {instance}\n\n")
        ext = filename.split('.')[-1]
        path = f'media/accounts/{instance.user, id}/images/'
        name = f'profile_image.{ext}'
        print(f"\nExt={ext}\nPath={path}\nName={name}\n")
        return os.path.join(path, name)


user_profile_image_path = GenerateProfileImagePath()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
