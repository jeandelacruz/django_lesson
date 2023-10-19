from django import forms
from .models import Author


# Ejemplo
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
