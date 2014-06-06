from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=140, blank=False)
    date=models.DateTimeField(auto_now_add=True)
    summary=models.TextField(blank=False)
    typ=models.CharField(max_length=50, blank=False)
    location=models.FilePathField(path='/srv/django/main/core/static/me',recursive=True)
# add models.FieldField(uploadto=???
#add a tags line for easy filtering

    def __unicode__(self):
        return self.title


class Entry(models.Model):
    title=models.CharField(max_length=140, blank=False)
    date=models.DateTimeField(auto_now_add=True)
    summary=models.TextField(blank=False)
    typ=models.CharField(max_length=50, blank=False)
    location=models.FilePathField(path='/srv/django/main/core/static/me',recursive=True)
    hide=models.BooleanField(default=False)
    readable_id=models.CharField(max_length=140, unique=True, blank=False)

# add models.FieldField(uploadto=???
#add a tags line for easy filtering

    def __unicode__(self):
        return self.title
