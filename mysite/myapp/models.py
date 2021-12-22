from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Song(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to=user_directory_path)
    audio = models.FileField(upload_to='music/%Y-%m-%d')


    def __str__(self):
        return self.title