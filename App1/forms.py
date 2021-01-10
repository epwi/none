from django import forms
from django.forms import TextInput
from .models import Ticket


class ADDTicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ('title',)
		widgets = {'title':TextInput(attrs={'class':'form-control'})}