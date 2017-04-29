from django import forms
from django.forms import Textarea
from django.forms import formset_factory, BaseFormSet
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


from .models import Article, Author, AuthorForm

class MyField(forms.CharField):
	# def to_python(self, value):
	# 	if not value:
	# 		return []
	# 	return value.split(',')

	# def validate(self, value):
	# 	super(MyField, self).validate(value)
	# 	for val in value:
	# 		if int(val)% 2!=0 :
	# 			raise forms.ValidationError(_("Please enter all fields as even number"))
	pass

class MyForm(forms.Form):
	data = forms.CharField()

	# def clean(self):
	# 	# super(MyForm, self).clean()
	# 	# #below 3 lines are must
	# 	if any(self.errors): #self.errors will automatically call super.clean() but still provide that

	# 		return
		
	# 	#if self.is_valid():
	# 	value = self.cleaned_data['data'] # ACCESS DATA ONLY IF FORM IS VALID, OR YOU HAVE RETURNED IF ANY(SELF.ERRORS)
	# 	if int(value)%2 != 0:			  # ....ELSE IT WILL GIVE KEY 'DATA' ERROR
			
	# 		raise forms.ValidationError(_("Please enter an even number"))
	
		
#NOTES:
# EITHER YOU DO 
# 1. INCLUDE REUTRN STATEMENT (IF ANY(SELF.ERROR))
# 2. OR, DO SELF.is_valid() BEFORE ACCESSING SELF.cleaned_data

# AND NOW THAT YOU HAVE DONE IT, INSIDE THE BaseAuthorFormSet, ...
# 	...YOU DON'T HAVE TO DO ANY CHECKING FOR IF FORM.IS_VALID (INSIDE FOR LOOP: FOR FORM IN SELF.FORMS)...
# 	...BECAUSE (concept: by doing if form.is_valid, we would try to avoid the error in the case when the...
# 	...form is submitted empty, because then the num=form.cleaned_data['data'] would raise the key 'data'...
# 	...error (because the form was submitted empty and hence the error) ,
# 	...But we know that before running the 'clean' method of the formset, django runs the 'clean' method of ..
# 	...the individual fields and hence the possibility of error when the form is submitted empty is handled..
# 	...by the clean method of individual fields, so we can directly [and safely:) :)]...
# 	...  do num = form.cleaned_data['data']

#THIS MUST BE DONE FOR BOTH 'FORM' OR 'FORMSET' BOTH:

#CUSTOM VALIDATION ERRORS SET IN 'CLEAN' METHOD OF BASEAUTHORFORMSET COMES UNDER FORM.NON_FORMS_ERRORS..
#..EVEN THE CUSTOM ERRORS OCCURING INSIDE 'CLEAN' METHOD OF FORM, FROM WHICH THE FORMSET IS MADE, COMES..
#..FORMS.ERRORS ONLY


# #non_field_error:
# ==>applied on forms.
# ==>form.non_field_errors() is the subset of form.errors and it include those errors which are...
# ...defined inside the 'clean' method of form

# #non_form_error
# ==>applied on formset (VVI) [DON'T APPLY BY ITERATING OVER INDIVIDUAL FORMS IN A FORMSET!!!]
# ==>formset.non_form_errors() is the subset of formset.errors and it include those errors which are..
# ..defined inside the 'clean' method of formset
# ==>Even the error occuring inside the 'clean' method of individual form(which will be...
# ... the part of form.non_field_errors() of that form) will NOT be included inside...
# ...formset.non_form_errors() ....ONLY THOSE ERRORS OCCURING INSIDE THE CLEAN METHOD OF FORMSET (DEFINED...
# ...INSIDE FORMSET CLASS)

# # example:
# in our form:
# ==> only "please enter an even number" error will be included inside the form.non_field_errors()
# ==> and all "required field" and "please enter an even number" error will be included in form.errors

# in our formset:
# ==> only "please enter distinct number in each field" error will be included in formset.non_form_errors()
# ==> and all "required field", "please enter even number", "please enter distinct number" in formset.errors



class BaseAuthorFormSet(BaseFormSet):
	def __init__(self, *args, **kwargs): #SUPPLY THIS IF YOU WANT THE 'REQUIRED FIELD' VALIDATION TO WORK 
		super(BaseAuthorFormSet,self).__init__(*args, **kwargs)
		# for form in self.forms:
		# 	form.empty_permitted=False
	# def clean(self):
	# 	# super(BaseAuthorFormSet, self).clean()
	# 	# print "self.errors = ", self.errors
	# 	if any(self.errors):
			
	# 		count=1
	# 		for form in self.forms:
	# 			print count, "non field error is", form.non_field_errors()
	# 			print count, "error is ", form.errors
	# 			count += 1
	# 		return
		
	# 	nums = []
	# 	for form in self.forms:
			
	# 		# if len(form.cleaned_data) == 0:
	# 		# 	print "fields empty"
	# 		# 	raise forms.ValidationError(_("All fields are required."))
	# 		#if form.is_valid():
	# 		num = form.cleaned_data['data']
	# 		if num in nums:
	# 			print "Please enter distinct number in each fields"
	# 			raise forms.ValidationError(_("Please enter distinct number in each fields"))

	# 		nums.append(num)

AuthorFormSet = formset_factory(MyForm, formset=BaseAuthorFormSet) #NOTE: WE HAVE NOT IMPORTED THIS CLASS 
												#... IN FORMS.PY, INSTEAD WE HAVE CREATED A SAME FORM FACTORY
												# ...IN THE VIEW.PY FILE FOR 'MODELFORM' VIEW METHOD.


class TestAuthorForm(AuthorForm):
	name = 'None'


	class Meta(AuthorForm.Meta):
		pass
		










