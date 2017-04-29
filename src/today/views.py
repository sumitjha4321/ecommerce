from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelformset_factory, formset_factory

from .forms import MyForm, TestAuthorForm, BaseAuthorFormSet
from .models import Article, AuthorForm, Author


def home(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():

			return HttpResponse("thanks")
	else:
		form = MyForm()
	context = {
		'form': form,
	}
	
	return render(request, 'todayhome.html', context)

# def formset(request):
# 	authorformsetview = AuthorFormSet(request.POST or None)
	
# 	context = {
# 		'authorformset':authorformsetview,
# 		'non_form_errors' : authorformsetview.non_form_errors(),

# 	}
# 	return render(request, "formset.html", context)

def formsetview(request):
	if request.method == "POST":
		formset = AuthorFormSet(request.POST)
		print formset.is_valid()
		if formset.is_valid():
			return HttpResponse("thanks")
	else:
		mydata = {
			'data' : 22,
		}

		formset = AuthorFormSet()
		context = {
			'formset' : formset,
		}
	return render(request, 'formset.html', {'formset':formset, 'non_form_errors': formset.non_form_errors()})
	#return render_to_response('formset.html', {'formset': formset})

def modelform(request):

	AuthorFormSet = formset_factory(MyForm, formset=BaseAuthorFormSet, extra=3)
	if request.method == 'POST':
		
		#form = AuthorForm(request.POST, instance = Author.objects.get(pk=1))
		forms = AuthorFormSet(request.POST)

		if forms.is_valid():
			forms.save()
			# for form in forms:
			
			# 	f = form.save(commit=False)
			# 	f.name = f.name + '3'
			# 	f.save()
			print "saved"
			return HttpResponse("Saved successfullly")

	else:
		#form = AuthorForm(instance = Author.objects.get(pk=1))
		forms = AuthorFormSet()
	context = {
		'form' : forms,
		'non_form_errors' : forms.non_form_errors(),
	}
	return render(request, 'modelform.html', context)

"""
def modelform(request):
	formset = modelformset_factory(Author, fields=('name','title','birth_date'))
	if request.method == 'POST':
		
		#form = AuthorForm(request.POST, instance = Author.objects.get(pk=1))
		
		forms = formset(request.POST)
		
		if forms.is_valid():
			
			for form in forms:
				#f = form.save(commit=False)
				#print f.cleaned_data
				#f.name= f.name.lower()
				#f.instance.name = f.name.upper()#f.instance.name + '2'
				f = form
				f.cleaned_data['name'] = f.instance.name.lower()
				f.save()


			#form.save()
		
			
			
			return HttpResponse("Saved successfullly")

	else:
		#form = AuthorForm(instance = Author.objects.get(pk=1))
		forms = formset()
	context = {
		'form' : forms,
	}
	return render(request, 'modelform.html', context)

"""


#ModelFormSet = modelformset_factory(Author, fields = ('__all__',))

# def modelformfactory(request):
# 		modelformset = ModelFormSet(queryset = Author.objects.filter(name__startswith='sumit'))
# 		context = {
# 			'modelformset' : modelformset,
# 		}
# 		return render(request, 'modelformsetfactory.html', context)

def modelformfactory(request):
	if request.method == 'POST':
		modelformset = TestAuthorForm(request.POST)
		if modelformset.is_valid():
			modelformset.save()
			return HttpResponse("thanks")

	else:
		modelformset = TestAuthorForm()

	context = {
		'modelformset' : modelformset,
	}
	return render(request, 'modelformsetfactory.html', context)





