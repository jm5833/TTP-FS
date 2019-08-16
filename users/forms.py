from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

#create a custom usercreationform 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = (
                'first_name', 
                'last_name', 
                'email',
                'password1',
                'password2'
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

#custom user login form
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        fields = ('email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email:
            raise forms.ValidationError('Please type in your email')
        elif not password:
            raise forms.ValidationError('Password cannot be blank')
        
