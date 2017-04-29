from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import AddressForm, UserAddressForm
from .models import UserAddress, UserCheckOut
from .mixins import CartOrderMixin

class AddressFormView(CartOrderMixin, FormView):
	form_class = AddressForm
	template_name = "orders/address_select.html"


	def dispatch(self, *args, **kwargs):
		print "dispatch.................................."
		b_address, s_address = self.get_address(*args, **kwargs)

		if b_address.count() == 0:
			messages.success(self.request, "Please add a billing address")
			return redirect("create_address") # REVERSE WILL RETURN 'UNICODE HAS NO ATTRIBUTE GET'

		elif s_address.count() == 0:
			messages.success(self.request, "Please add a shipping address")
			return redirect("create_address") # REVERSE WILL RETURN 'UNICODE HAS NO ATTRIBUTE GET'
		return super(AddressFormView, self).dispatch(*args, **kwargs)



		



	def get_address(self, *args, **kwargs):
		user_checkout_id = self.request.session.get("user_checkout_id")
		

		user_checkout = UserCheckOut.objects.get(id=user_checkout_id) # FIX THIS...
		print "user_checkout_id is", user_checkout_id 

		b_address = UserAddress.objects.filter(
			user=user_checkout,
			type='billing',

			)

		s_address = UserAddress.objects.filter(
			user=user_checkout,
			type='shipping',

			)
		return b_address, s_address


	def get_form(self, *args, **kwargs):
		print "get_form.................................."

		form = super(AddressFormView, self).get_form(*args, **kwargs)
		b_address, s_address = self.get_address()
		form.fields["billing_address"].queryset =  b_address

		form.fields["shipping_address"].queryset =  s_address
		return form

	def form_valid(self, form, *args, **kwargs):
		print "form_valid.................................."

		#print form.cleaned_data----BOTH 'form.CLEANED_DATA' AND 'form.FIELDS' ARE ACCESSIBLE ONLY BEFORE CALLING SUPER-FORM_VALID METHOD
		#print form.fields

		billing_address = form.cleaned_data["billing_address"]
		shipping_address = form.cleaned_data["shipping_address"]
		order = self.get_order()
		order.shipping_address = shipping_address
		order.billing_address = billing_address
		order.save()
		# self.request.session["billing_address_id"] = billing_address.id
		# self.request.session["shipping_address_id"] = shipping_address.id


		return super(AddressFormView, self).form_valid(form, *args, **kwargs)
		
	
		return form 

	def get_success_url(self, *args, **kwargs):
		return reverse("checkout")


class UserAddressCreateView(CreateView):
	form_class = UserAddressForm
	template_name = "forms.html" # SEE THIS
	success_url = "/checkout/address"

	def get_checkout_user(self):
		user_checkout_id = self.request.session.get("user_checkout_id")
		user_checkout = UserCheckOut.objects.get(id=user_checkout_id) # FIX THIS...
		return user_checkout

	def form_valid(self, form, *args, **kwargs):
		form.instance.user = self.get_checkout_user()
		return super(UserAddressCreateView, self).form_valid(form, *args, **kwargs)



