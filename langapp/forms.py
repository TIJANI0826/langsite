from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_registration.forms import RegistrationForm


class UserRegisterForm(UserCreationForm):
    """
    docstring for UserRegisterForm"UserCreationFormf __init__(self, arg):
    super(UserRegisterForm,UserCreationForm.__init__()
    self.arg = arg
    """
    email = forms.EmailField()

    class Meta:
        """
        docstring for Meta: __init__(self, arg):
        super(Meta:_init__()
        self.arg = arg
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# class RegistrationForm(UserCreationForm):
#     username  =
#     email
#     password2 =
#     password

from django import forms
from .models import ContactForm
from django.forms import ModelForm

"""class ContactForm(forms.Form):
    name = forms.CharField(label='Your name')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

"""


class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'

