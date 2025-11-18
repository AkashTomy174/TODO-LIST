from django import forms
from .models import contactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactMessage
        fields = ['name', 'email', 'message', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
