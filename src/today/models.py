from django.db import models
from django import forms

from products.models import Product

class Article(models.Model):
	pub_date = models.DateTimeField() 
	headline = models.CharField(max_length = 200)
	content = models.CharField(max_length = 200)
	reporter = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.headline

TITLE_CHOICES = (

	('MR', 'Mr.'), # (key, value) -- and value will be displayed in the select list
	('MRS', 'Mrs.'),
	('MS', 'Ms.'),
)


class Author(models.Model):
	name = models.CharField(max_length=100, blank=False, null = False)
	title = models.CharField(max_length=100, choices = TITLE_CHOICES)
	birth_date = models.IntegerField()

	def __unicode__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)


class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['birth_date', 'title', ] # REQUIRED, ELSE IMPROPERLY CONFIGURED EXCEPTION IS RAISED
		

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['name', 'authors']


class Publication(models.Model):
	title = models.CharField(max_length=120)

	def __unicode__(self):
		return self.title


class Article2(models.Model):
	headline = models.CharField(max_length=120)
	publications = models.ManyToManyField(Publication)

	def __unicode__(self):
		return self.headline

class Person(models.Model):
	name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Person, through='Membership')
	
	def __unicode__(self):
		return self.name


class Membership(models.Model):
	person = models.ForeignKey(Person)
	group = models.ForeignKey(Group)
	date_joined = models.DateField()
	invite_reason = models.CharField(max_length=64)

