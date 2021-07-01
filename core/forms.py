from django import forms
from django.forms import ModelForm 
from .models import Libro

class LibrosForm(ModelForm):
    
    class Meta:
        model = Libro
        fields = ['isbn', 'nombre', 'autor', 'categoria',]