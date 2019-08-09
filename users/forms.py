from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#create a custom usercreationform that also accepts name and email
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'name', 
            'email',
            'username',
            'password1',
            'password2'
        )

    #overwrite save function to save the additional information
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

