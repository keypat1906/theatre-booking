from django import forms

from .models import Url

from django import forms
from django.utils.translation import ugettext_lazy as _          
from django.core.validators import RegexValidator


class ShortUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('url',)

class LongUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('url',)
