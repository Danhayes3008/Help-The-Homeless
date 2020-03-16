from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('name', 'gender', 'nationality', 'birthday', 'image')
# This form allows us to delete our accounts
class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.
# This is used to log the user into the site
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
# This form allows the user to create an account
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'E-mail already in use!')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2
 # This form is used to update the user table    
class updateUserForm(forms.ModelForm):
    username= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'username'}))
    email= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'email address'}))
    class Meta:
        model = User
        fields = ['username', 'email']
# This form is used to update the profile table        
class updateProfileForm(forms.ModelForm):
    name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'name'}))
    gender= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'gender'}))
    nationality= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'nationality'}))
    birthday= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'yyyy-mm-dd'}))
    class Meta:
        model = Profile
        fields = ['name', 'image', 'gender', 'nationality', 'birthday']