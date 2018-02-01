from django.conf.urls import url
from contacts.views import Index
from . import views

urlpatterns = [
	url('', Index.as_view(), name='home'),
]