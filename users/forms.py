from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	"""docstring for UserRegisterForm"UserCreationFormf __init__(self, arg):
		super(UserRegisterForm,UserCreationForm.__init__()
		self.arg = arg
	"""
	email = forms.EmailField()

	class Meta:
		"""docstring for Meta: __init__(self, arg):
			super(Meta:_init__()
			self.arg = arg
		"""
		model = User
		fields = ['username', 'email', 'password1','password2']