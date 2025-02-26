from django import forms
from .models import Author, Quote , Tag
from django.forms import ModelForm, CharField, TextInput



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

# class QuoteForm(forms.ModelForm):
#     class Meta:
#         model = Quote
#         fields = ['quote', 'tags', 'author']


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
        widgets = {
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }