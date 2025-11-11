from django import forms
from .models import Listing

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ListContact(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = Listing.listing_id