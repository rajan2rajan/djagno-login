from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForms(UserCreationForm):
    email = forms.CharField(label="Email",widget=forms.EmailInput,required=True)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_email(self):
        valemail = self.cleaned_data['email']
        if User.objects.filter(email = valemail).exists():
            raise forms.ValidationError('this email already exit ')
        return valemail
    
    # R9865177862