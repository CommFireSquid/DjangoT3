from django.db import models

class ContactTable(models.Model):
	#cid = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=100)
	midName = models.CharField(max_length=100,null=True)
	lastName = models.CharField(max_length=100)
	phone = models.IntegerField(null=True)
	email = models.CharField(max_length=100,null=True)
	note = models.CharField( max_length=255,null=True)
	date = models.DateTimeField(auto_now=True)