from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django import forms
from contacts.models import ContactTable

class ContactForm(forms.ModelForm):
	firstName = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'Jon'}))
	midName = forms.CharField(required=False,label='Middle Name (or Initial)',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'Adam'}))
	lastName = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'Doe'}))
	phone = forms.IntegerField(required=False,label='Phone',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': '18005559797'}),validators=[RegexValidator(r'^\d{1,10}$',message="Enter a valid phone number")])
	email = forms.CharField(required=False,label='Email',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'jdoe@example.com'}),validators=[EmailValidator()])
	comment = forms.CharField(label='Note',required=False,widget=forms.Textarea )
	cid = forms.IntegerField(label='CID',required=False,widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'Optional'}))

	class Meta:
		model = ContactTable
		fields = ('firstName','midName','lastName','phone','email')

class SearchForm(forms.Form):
	searchValueF = forms.CharField(label='',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder':'Jon'}))
	searchValueM = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder':'M'}))
	searchValueL = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder':'Doe'}))
	searchValueP = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder':'18005559797'}))

class DeleteForm(forms.Form):
	deleteCID = forms.IntegerField(label='CID To Delete',widget=forms.TextInput(attrs={'style':'border-radius:5px','placeholder': 'CID To Delete'}))