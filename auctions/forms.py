
from django import forms
from .models import Listing
  
class AddListingForm(forms.ModelForm):
  
    class Meta:
        model = Listing
        fields = ('image', 'listingTitle', 'description', 'currentBid', 'category')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }