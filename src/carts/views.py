from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.core.exceptions import MultipleObjectsReturned
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormMixin

from products.models import Variation
from .models import CartItem, Cart
from orders.forms import GuestCheckOutForm
from orders.models import UserCheckOut, Order, UserAddress
from orders.mixins import CartOrderMixin


# all page calls this view (BY AJAX METHOD)
# because in javascript.html , we have written a script to that calls this view by ajax method
# check javascript.html

class CartItemCount(View): 
	def get(self, request, *args, **kwargs):

		if self.request.is_ajax():
			
			cart_id = self.request.session.get("cart_id")

			
			
			cart = Cart.objects.get(id=cart_id)
			count = cart.cartitem_set.count() #note that cart.items.count() [i.e counting variations], and
											# ..the cart.cartitem_set.count() gives the same number.
											#..tutorial did first way, i did second.
			
			request.session["cart_item_count"] = count								
			return JsonResponse({
				"count" : count,
				})
		else:
			raise Http404

class CartView(SingleObjectMixin, View):

	model = Cart # Don't forget to set this !!
	template_name = "carts/view.html"

	def get_object(self, *args, **kwargs):

		self.request.session.set_expiry(0)
		
	


		# """
		# REMOVING THESE LINE AND THIS WILL HAPPEN:
		# --IF YOU LOG OUT, AND LOG IN AGAIN, A NEW CART WILL BE CREATED FOR YOU 
		# --BECAUSE THE SESSION DATA IS CLEARED WHEN YOU LOG OUT
		# --HENCE IN THE DATABASE, YOU WILL HAVE MULTIPLE CART WITH NAME=SUMIT
		#(note that if you close the browser, then we expire our session data, hence we are prompted to login again and hence again new cart will be created)
 	 	# if self.request.user.is_authenticated():
		# # 	cart = Cart.objects.filter(user=self.request.user)
			
		# # 	if cart.count() > 0:
		# # 		return cart[0]
		# """
			
		
		
		# print "here....................................."
		
		cart_id = self.request.session.get("cart_id")
		print "cart_id is ", cart_id
		
		
		if cart_id == None:
			
			cart = Cart()
			cart.save()
			cart_id = cart.id
			
			self.request.session["cart_id"]=cart_id
		cart = Cart.objects.get(id=cart_id)
		if self.request.user.is_authenticated():
			cart.user = self.request.user
			cart.save()
		return cart


	def get(self, request, *args, **kwargs):
		
		cart = self.get_object()

		item_id = self.request.GET.get("item_id")
		quantity = self.request.GET.get("quantity", 1)

		
		delete_item = self.request.GET.get('delete')
		
		if int(quantity) < 1:
			delete_item = True

		message = "" # AJAX Message

		if item_id:

			item_instance = get_object_or_404(Variation, id=item_id)
			
			#cart = Cart.objects.all().first()
			new_cartitem = CartItem.objects.get_or_create(cart=cart, items=item_instance)
			
			

				# NOTE: new_cartitem is like (<CartItem: 16GB>, False)
				#.....so do [0] or [1] accordingly
			
			if delete_item:
				
				new_cartitem[0].delete()
				cart.update_subtotal() #we do this "EXPLICITLY" to update subtotal in case we delete the item from cart.
				cart.update_tax_and_total()					# we don't have to call this explicitly in case of save because in that case the
									# post receiver function would automatically call this.
									#OR make a post_delete receiver

				#message = new_cartitem[0].items.product + "( " + new_cartitem[0].items     "Item removed successfully."					
				message = "Item removed successfully."
			else:
				# if new_cartitem[1]==False:
				# 	new_cartitem[0].quantity = int(new_cartitem[0].quantity) + int(quantity)
				
				new_cartitem[0].quantity = int(quantity)
				new_cartitem[0].save()
				if new_cartitem[1] == True:
					message = "Item added successfully."
				else:
					message = "Item updated successfully."

			# if not request.is_ajax():
			# 	return HttpResponseRedirect(reverse('cartview'))


		if request.is_ajax():
			if item_id:
				line_total =  new_cartitem[0].line_item_total
				subtotal = new_cartitem[0].cart.subtotal
				tax_total = new_cartitem[0].cart.tax_total
				total = new_cartitem[0].cart.total
			
				#if request is ajax, will return from
				# here only..
				# add here what data you want to pass
				# like 'contenxt'variable
				
				return JsonResponse({						
				
					'line_item_total' : line_total,
					'subtotal' : subtotal,
					'tax_total' : tax_total,
					'total' : total,
					'message' : message,
					'items_remaining_in_cart' : cart.cartitem_set.count(),
				}) 
			else:
				return JsonResponse({
					'message' : "Item removed successfully."
					});
														
		
		context = {
			"object" : self.get_object()
		}
		template = self.template_name
		
		return render(request, template, context)



class CheckOutView(CartOrderMixin, FormMixin, DetailView):
	model = Cart
	template_name = "carts/checkoutview.html"
	form_class = GuestCheckOutForm # an attribute of FormMixin which gives the name of class to instantiate

	# def get_order(self):
	# 	new_order_id = self.request.session.get("order_id")
	# 	cart = self.get_object()
	# 	if new_order_id is None:
	# 		new_order = Order.objects.create(cart=cart)
	# 		self.request.session["order_id"] = new_order.id
	# 	else:
	# 		new_order = Order.objects.get(id = new_order_id)

	# 	return new_order



	def get_object(self):
		#cart_id = self.request.session.get("cart_id")
		cart = self.get_cart()
		
		if cart == None:
			return None
		return cart

	def get_context_data(self, *args, **kwargs):
		
		context = super(CheckOutView, self).get_context_data(*args, **kwargs)
		user_can_continue = False
		#context["auth_user"] = self.request.user.is_authenticated()
		context["order"] = self.get_order()

		user_checkout_id = self.request.session.get("user_checkout_id")
		if not self.request.user.is_authenticated() or user_checkout_id == None: 
			
			context["login_form"] = AuthenticationForm()
			context["next_url"] = self.request.build_absolute_uri()
			context["form"] = self.get_form() #FormMixin method to instantiate an instance of 'form_class'
					                          #...defined above in this view.
												#...This method gets the name of the class(more specically, form-class)
												#...from the 'form_class' itself, if that's not available, it calls the
												#...method get_form_class()
												#...see documentation, page-634/640


		if self.request.user.is_authenticated():
			#user_checkout, created = UserCheckOut.objects.get_or_create(email=UserCheckOut.objects.filter(user=self.request.user))
			user_checkout, created = UserCheckOut.objects.get_or_create(email=self.request.user.email) #TUTORIAL
			user_can_continue = True
			self.request.session["user_checkout_id"] = user_checkout.id # MUST DO THIS STEP, BECAUSE WHEN THE USER IS AUTHENTICATED, YOU ARE SETTING USER_CAN_CONTINUE TO TRUE, HENCE GUEST/LOGIN FORM WILL NEVER BE DISPLAYED AND HENCE USER_CHECKOUT_ID WILL NEVER BE FILLED IN THE SESSION DATA
		elif user_checkout_id != None:
			user_can_continue = True


		context["user_can_continue"] = user_can_continue
		



		return context


	def post(self, request, *args, **kwargs):
		form = self.get_form()                       # similar to what we did in function based CartView
														#...form = ContactForm(request.post or None)...

		self.object = self.get_object()
		if form.is_valid():				
			email = form.cleaned_data["email"]
			user_checkout, created = UserCheckOut.objects.get_or_create(email=email) #i just followed the tutorial here
												# ..get_or_create call is not necessary here because we have 
												# already defined a clean_email method in forms.py which will 
												# not allow to enter duplicate email.
												# However, it may be necessary if you are raising "a user with that email"
												#..validation error (ie duplicate email error) using USER MODEL.
												# AS OF NOW, I HAVE USED USERCHECKOUT MODEL

												#After CT, i removed get_or_create call and put just get call.

			request.session["user_checkout_id"] = user_checkout.id
			print "setting user_checkout_id............................."
			return self.form_valid(form)
		else:
			return self.form_invalid(form)


	def get_success_url(self):
		return reverse("checkout")

	def get(self, request, *args, **kwargs):
	

		get_data = super(CheckOutView, self).get(request, *args, **kwargs)

		cart = self.get_object()
		new_order = self.get_order()
		if cart.items.count() <=0 :
			return redirect("cartview")
		user_checkout_id = request.session.get("user_checkout_id")
		print "user_checkout_id is ", user_checkout_id
		if user_checkout_id != None:
			user_checkout = UserCheckOut.objects.get(id=user_checkout_id)
		
		else: # return from 'get' request, display the Guest/login form, make post request, fill 'user_checkout_id' and then proceed
		
			return get_data

		# billing_address_id = request.session.get("billing_address_id")
		# shipping_address_id = request.session.get("shipping_address_id")

		if new_order.billing_address == None or new_order.shipping_address == None:
			print "redirecting to order address"
			#request.session["user_checkout_id"] = user_checkout.id #not done on tutorial 
			return redirect("order_address")
		# else:
		# 	billing_address = UserAddress.objects.get(id=billing_address_id)
		# 	shipping_address = UserAddress.objects.get(id=shipping_address_id)

		# try:
		# 	new_order_id = request.session["order_id"]
		# 	new_order = Order.objects.get(id = new_order_id)
		# except:
		# 	new_order = Order()
		# 	request.session["order_id"] = new_order.id


 
		new_order.user = user_checkout
		# new_order.billing_address = billing_address
		# new_order.shipping_address = shipping_address
		new_order.save()

		return get_data


#USER_CHECKOUT_ID FOR AUTHENTICATED USER IS SET INSIDE GET_CONTEXT_DATA AND ..
#..FOR GUEST, IT IS SET INSIDE POST METHOD FOR 'CHECKOUTVIEW'