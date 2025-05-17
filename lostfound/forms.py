from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LostItem

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    contact_number = forms.CharField(max_length=15, required=False, label="Contact Number")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.contact_number = self.cleaned_data['contact_number']
            user.profile.save()
        return user

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'location', 'image', 'category']