from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Freizeittipp(models.Model):
    id = models.UUIDField()
    is_published = models.BooleanField(default=False, verbose_name="Veröffentlicht?")
    title = models.CharField(max_length=264)
    # category = TaggableManager()
    # tags = TaggableManager()  #https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
    # age_group =
    content = models.TextField()

    hp_link = models.URLField()
    tel = models.CharField(max_length=32)
    e-mail = models.EmailField(max_length=264, unique = True)
    created = models.DateField(auto_now_add=True, verbose_name="Erstellt am")
    updated_current = models.DateField(auto_now=True, verbose_name="Zuletzt geändert am")
    # rating =
    images = models.ImageField()


######## ADDRESS ############

# https://pypi.org/project/django-address/

# class Address(models.Model):
#     street = models.ForeignKey('StreetAddress')
#     city = models.TextField()
#     code = models.TextField()
#
# class StreetAddress(models.Model):
#     number = models.IntegerField()
#     name = models.TextField()
