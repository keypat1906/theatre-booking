from django import forms

from .models import Url

from django import forms


class ShortUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('url',)

class LongUrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('url',)
