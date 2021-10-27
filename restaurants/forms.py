from django import forms
from .models import Restaurant, Comment
from .snippets import choices


class RestaurantCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa el título'}))
    categories = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Categorías separadas por comas. Ejemplo: chino, tailandés'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa ubicación'}))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio'}))
    vat = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'IVA en %'}))
    taste = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=choices)
    persons = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=choices)
    details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Restaurant
        fields = ['title', 'image', 'categories', 'location',
                  'price', 'vat', 'taste', 'persons', 'details']
