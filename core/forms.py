from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# class LoginForm(AuthenticationForm):

#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your Username',
#         'name': 'username',
#         'class': 'w-full py-4 px-6 rounded-xl'}))

#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Your Password',
#         'name': 'password',
#         'class': 'w-full py-4 px-6 rounded-xl'}))
    
#     img = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id': 'img'}))

#     def clean_img(self):
#         img_data = self.cleaned_data['img']
#         if not img_data:
#             raise forms.ValidationError("Image data is required.")
#         # Additional validation logic for the image data if needed
#         return img_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'}), label='Username')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'}), label='Password')
    
    # img = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'img'}))

    # def clean_img(self):
    #     img_data = self.cleaned_data['img']
    #     if not img_data:
    #         raise forms.ValidationError("Image data is required.")
    #     # Additional validation logic for the image data if needed
    #     return img_data


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6 rounded-xl'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-full py-4 px-6 rounded-xl'}))

    # image = forms.ImageField()

