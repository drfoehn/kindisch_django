from django import forms
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Freizeittipp(models.Model):
    title = models.CharField(max_length=264, verbose_name="Titel")
    # tag = TaggableManager(verbose_name="Schlagworte")
    categories = models.ManyToManyField('category.Category', help_text='Kategorie angeben', default="blank")
    tags = models.ManyToManyField('category.Tag',help_text='Tags angeben', default="blank")
    age_from = models.IntegerField(default = 0, verbose_name="Geeignet für ein Alter von") #Filter Integer Range: https://stackoverflow.com/questions/33104897/django-filter-objects-by-integer-between-two-values
    age_to = models.IntegerField(default = 18, verbose_name="bis")
    freizeittipp_image = models.ImageField(upload_to = 'static/images/freizeittipps/', default = 'static/images/no-img.jpg', verbose_name="Freizeittipp-Bild")
    description = models.TextField(verbose_name="Beschreibung")
    hp_link = models.URLField(verbose_name="Homepage", default="blank")
    tel = models.CharField(max_length=32, verbose_name="Telefon-Nr", default="blank")
    email = models.EmailField(max_length=264, default="blank")
    is_published = models.BooleanField(default=False, verbose_name="Veröffentlicht?")
    created = models.DateField(auto_now_add=True, verbose_name="Erstellt am")
    updated_current = models.DateField(auto_now=True, verbose_name="Zuletzt geändert am")

# class Rating(models.Model):
    # rating =  https://django-star-ratings.readthedocs.io/en/latest/?badge=latest%2F

class ImageUploadForm(forms.Form): #https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    """
    Image upload form.
    """
    image = forms.ImageField()   #Get Pillow at https://pypi.org/project/Pillow/


# class Tags(models.Model):
#     tags = TaggableManager()  #https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704

# class Contact(models.Model):
#     hp_link = models.URLField(verbose_name="Homepage", default = 'keine Info vorhanden')
#     tel = models.CharField(max_length=32, verbose_name="Telefon-Nr", default = 'keine Info vorhanden')
#     email = models.EmailField(max_length=264, unique = True,  default = 'keine Info vorhanden')


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
