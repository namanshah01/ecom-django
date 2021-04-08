from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Id'})
		}
	
	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Set Password'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
	
		for fieldname in ['username', 'email', 'password1', 'password2']:
				self.fields[fieldname].help_text = None
				self.fields[fieldname].label = ''

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']
