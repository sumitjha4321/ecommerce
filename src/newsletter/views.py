from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp
from products.models import ProductFeatured, Category, Product

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)

	featured_image = ProductFeatured.objects.first()
	categories = Category.objects.all()
	context = {
		"title": title,
		"form": form,
		"featured_image":featured_image,
		"categories":categories,
		"products":Product.objects.all().order_by('?'),
	}
	
						# if request.user.is_authenticated() and request.user.is_staff:
						# 	#print(SignUp.objects.all())
						# 	# i = 1
						# 	# for instance in SignUp.objects.all():
						# 	# 	print(i)
						# 	# 	print(instance.full_name)
						# 	# 	i += 1

						# 	queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
						# 	#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
						# 	context = {
						# 		"queryset": queryset
						# 	}

	return render(request, "home.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)
















