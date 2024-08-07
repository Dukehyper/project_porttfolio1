# # portfolio/forms.py

# from django import forms
# from .models import Contact

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'about_project']
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
#             'about_project': forms.Textarea(attrs={'placeholder': 'About Project'}),
#         }


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'about_project']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': ' ', 'class': 'form-control name-input'}),
            'email': forms.EmailInput(attrs={'placeholder': ' ', 'class': 'form-control email-input'}),
            'about_project': forms.Textarea(attrs={'placeholder': ' ', 'class': 'form-control project-textarea'}),
        }
