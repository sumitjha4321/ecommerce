from .models import Order
from carts.models import Cart


class CartOrderMixin(object):
	def get_order(self):
		new_order_id = self.request.session.get("order_id")
		cart = self.get_cart()
		if new_order_id is None:
			new_order = Order.objects.create(cart=cart)
			self.request.session["order_id"] = new_order.id
		else:
			new_order = Order.objects.get(id = new_order_id)

		return new_order



	def get_cart(self):
		cart_id = self.request.session.get("cart_id")
		
		if cart_id == None:
			return HttpResponseRedirect(reverse('ProductListView'))
		cart = Cart.objects.get(id=cart_id)
		
		return cart

