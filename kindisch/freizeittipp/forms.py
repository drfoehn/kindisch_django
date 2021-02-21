from django import forms
from freizeittipp.models import Freizeittipp

class NewTippForm(forms.ModelForm):
    class Meta:
        model = Freizeittipp
        fields = '__all__'
