from django import forms
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Freizeittipp(models.Model):
    title = models.CharField(max_length=264, verbose_name="Titel")
    age_from = models.IntegerField(default = 0, verbose_name="Geeignet für ein Alter von") #Filter Integer Range: https://stackoverflow.com/questions/33104897/django-filter-objects-by-integer-between-two-values
    age_to = models.IntegerField(default = 18, verbose_name="bis")
    categories = models.ManyToManyField('category.Category', help_text='Kategorie angeben', blank="True")
    tag_taggit = TaggableManager(verbose_name="Schlagworte_taggit")
    tag = models.ManyToManyField('category.Tag',help_text='Tags angeben', blank="True", verbose_name="Schlagwort_category")
    freizeittipp_image = models.ImageField(upload_to = 'static/images/freizeittipps/', default = 'static/images/no-img.jpg', verbose_name="Freizeittipp-Bild")
    description = models.TextField(verbose_name="Beschreibung")
    city = models.CharField(max_length=126, verbose_name="Stadt", default='Salzburg')
    postal_code = models.PositiveIntegerField(verbose_name="PLZ", default='5020')
    street = models.CharField(max_length=126, verbose_name="Strasse, Nr", blank="True", null="True")
    country = models.CharField(max_length=126, verbose_name="Land", default='Österreich')
    hp_link = models.URLField(verbose_name="Homepage", blank="True", null="True")
    tel = models.CharField(max_length=32, verbose_name="Telefon-Nr", blank="True", null="True")
    email = models.EmailField(max_length=264, default="blank")
    is_published = models.BooleanField(default=False, verbose_name="Veröffentlicht?")
    created = models.DateField(auto_now_add=True, verbose_name="Erstellt am")
    updated_current = models.DateField(auto_now=True, verbose_name="Zuletzt geändert am")
    # Manager
    objects = models.Manager() #https://docs.djangoproject.com/en/3.1/topics/db/managers/

    def __str__(self):
        return self.title

class ImageUploadForm(forms.Form): #https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield
    """
    Image upload form.
    """
    image = forms.ImageField()   #Get Pillow at https://pypi.org/project/Pillow/




# class Rating(models.Model):
    # rating =  https://django-star-ratings.readthedocs.io/en/latest/?badge=latest%2F

# class Address(models.Model):
#     city = models.CharField(max_length=126, verbose_name="Stadt", default='Salzburg')
#     postal_code = models.PositiveIntegerField(verbose_name="PLZ", default='5020')
#     street = models.CharField(max_length=126, verbose_name="Strasse, Nr")
#     country = models.CharField(max_length=126, verbose_name="Land", default='Österreich')
#
#     def __str__(self):
#         return self.name
#
# class Contact(models.Model):
#     hp_link = models.URLField(verbose_name="Homepage", default="blank")
#     tel = models.CharField(max_length=32, verbose_name="Telefon-Nr", default="blank")
#     email = models.EmailField(max_length=264, default="blank")
#
#     def __str__(self):
#         return self.name
#
# class Category_freizeittipp(models.Model):
#     categories = models.ManyToManyField('category.Category', help_text='Kategorie angeben', default="blank")
#
#     def __str__(self):
#         return self.name
#
# class Tag_freizeittipp(models.Model):
#     tag_taggit = TaggableManager(verbose_name="Schlagworte_taggit")
#     tag = models.ManyToManyField('category.Tag',help_text='Tags angeben', default="blank")
#
#     def __str__(self):
#         return self.name
#
