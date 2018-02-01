from django.views.generic import TemplateView
from django.shortcuts import render
from contacts.forms import ContactForm
from contacts.forms import SearchForm
from contacts.forms import DeleteForm
from contacts.models import ContactTable
import sqlite3

'''def index(request):
	return render(request, 'contacts/home.html')'''


class Index(TemplateView):
	template_name = 'contacts/home.html'

	def get(self, request):
		contactsForm = ContactForm()
		searchForm = SearchForm()
		deleteForm = DeleteForm()
		result = 'Output from searches and data entry will display here'
		args = {'deleteForm':deleteForm, 'searchForm':searchForm, 'contactsForm':contactsForm, 'result':result}
		return render(request, self.template_name, args)

	def post(self, request):
		result = 'ERROR'
		form = ContactForm(request.POST)
		contactsForm = ContactForm()
		form2 = SearchForm(request.POST)
		searchForm = SearchForm()
		form3 = DeleteForm(request.POST)
		deleteForm = DeleteForm()

		if form.is_valid():
			firstName = form.cleaned_data['firstName']
			midName = form.cleaned_data['midName']
			lastName = form.cleaned_data['lastName']
			phone = form.cleaned_data['phone']
			email = form.cleaned_data['email']
			comment = form.cleaned_data['comment']
			cid = form.cleaned_data['cid']


			if cid == None:
				form.cleaned_data['cid'] = 1
				form.save()
				result = 'Data Saved'
			else:
				count = ContactTable.objects.filter(id=cid).count()
				if count == 1:
					callBack = ContactTable.objects.get(id=cid)
					callBack.firstName = firstName
					callBack.midName = midName
					callBack.lastName = lastName
					callBack.phone = phone
					callBack.email = email
					callBack.comment = comment
					callBack.cid = cid
					callBack.save()
					result = 'Contact Updated'
				else:
					result = 'Contact Not Found'
					contactsForm = form


			args = {'deleteForm':deleteForm, 'searchForm':searchForm, 'contactsForm':contactsForm, 'result':result}
			return render(request, self.template_name, args)
		
		elif form2.is_valid():
			searchItem = form2.cleaned_data['searchValueF']
			searchItem2 = form2.cleaned_data['searchValueM']
			searchItem3 = form2.cleaned_data['searchValueL']
			searchItem4 = form2.cleaned_data['searchValueP']

			result = searchItem
			args = {'deleteForm':deleteForm, 'searchForm':searchForm, 'contactsForm':contactsForm, 'result':result}
			return render(request, self.template_name, args)

		elif form3.is_valid():
			deleteCID = form3.cleaned_data['deleteCID']

			if deleteCID != None:
				if deleteCID == 0:
					ContactTable.objects.all().delete()
					result = 'Contact List Cleared'
				else:
					ContactTable.objects.filter(id = int(deleteCID)).delete()
					result = 'Contact with CID: {} deleted'.format(deleteCID)

			args = {'deleteForm':deleteForm, 'searchForm':searchForm, 'contactsForm':contactsForm, 'result':result}
			return render(request, self.template_name, args)
		else:
			result = 'Invalid Entry'
			contactsForm = form
			searchForm = form2
			deleteForm = form3
			args = {'deleteForm':deleteForm, 'searchForm':searchForm, 'contactsForm':contactsForm, 'result':result}
			return render(request, self.template_name, args)