from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Create your forms here.

class NewUserForm(forms.ModelForm):
	

	class Meta:
		model = User
		fields = ("name", "familyName", "email", "password")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class updateUserForm(forms.ModelForm):
	

	class Meta:
		model = User
		fields = ("name", "familyName", "email")

	def save(self, commit=True):
		user = super(updateUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user