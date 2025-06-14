from django import forms
from .models import Resume
from django.contrib.auth.models import User

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'full_name',
            'email',
            'phone',
            'summary',
            'education',
            'experience',
            'skills',
            'projects',
        ]
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 2}),
            'projects': forms.Textarea(attrs={'rows': 3}),
        }

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
