from django import forms

from .models import ContactUs, Newsletter, Reports, Dogs, User, Adoption

class ContactUsForm(forms.ModelForm):
    # model forms
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={
                'cols': 40, 'rows': 5, 'placeholder': 'Message',
                'class': 'form-control my-2'
                }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control my-2'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control my-2'
                })

        }

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_name',
            'user_contact',
            'user_email'
        ]
        widgets = {
            'user_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control my-2'
            }),
            'user_contact': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control my-2'
            }),
            'user_email': forms.TextInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control my-2'
            }),
        }

class AdoptionDogDetailsForm(forms.ModelForm):
    class Meta:
        model = Dogs
        fields = [
            'dog_name'
        ]
        widgets = {
            'dog_name': forms.TextInput(attrs={
                'placeholder': "Dog's Name",
                'class': 'form-control my-2'
            }),
        }
class MissingDogForm(forms.ModelForm):
    # model forms
    class Meta:
        model = Reports
        fields = [
            'dog',
            'breed',
            'reporter',
            'last_known_location',
            'category'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }

class NewsletterForm(forms.ModelForm):
    # model forms
    class Meta:
        model = Newsletter
        fields = '__all__'