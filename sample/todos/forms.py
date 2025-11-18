from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter todo title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description (optional)', 'rows': 3}),
        }
