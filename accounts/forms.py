from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
	captcha = CaptchaField()
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		is_exists = User.objects.filter(username=username).exists()
		if not is_exists:
			raise forms.ValidationError("NOT FOUND")
		return username
