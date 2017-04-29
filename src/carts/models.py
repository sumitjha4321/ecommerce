from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save

from decimal import Decimal


from products.models import Variation

class CartItem(models.Model):
	cart = models.ForeignKey('Cart')
	items = models.ForeignKey(Variation)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.items.title

	def remove(self):
		#return "%s?item_id=%s&delete=True"%(reverse('cartview'), self.items.id)
		return self.items.remove_from_cart() # we have implemented an instance method on 'Variation' model itself.
											 # ... we could do as above also.
											 # 'self' refers to 'CartItem' instance,
											 # 'self.items' refers to 'Variation'

	def get_price(self):
		
		return self.items.product.price

	def get_title(self): #implemented this method after end sem , while doing checkoutview. just for practice. used inside "checkoutview.HTML"
		return self.items.product.title + " (" + self.items.title + ")"


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
	quantity = instance.quantity
	price = instance.get_price()
	instance.line_item_total = Decimal(quantity) * Decimal(price)

	

def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
	instance.cart.update_subtotal()
	instance.cart.update_tax_and_total()
	

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)
post_save.connect(cart_item_post_save_receiver, sender=CartItem)


class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	items = models.ManyToManyField(Variation, through=CartItem)
	#items2 = models.ManyToManyField(Variation, through=CartItem)
	#items5 = models.ManyToManyField(Variation, through=CartItem)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)
	subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	tax_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


	def __unicode__(self):
		return (str(self.id))


	def update_subtotal(self):
		items = self.cartitem_set.all()
		subtotal = 0
		for item in items:
			subtotal += item.line_item_total
		self.subtotal =  "%.2f" %(subtotal)
		self.save()

	def update_tax_and_total(self):
		subtotal = self.subtotal
		tax_total = Decimal(subtotal)*Decimal(0.07)
		total = Decimal(subtotal) + tax_total
		self.tax_total = "%.2f" %(round(tax_total, 2))
		self.total =  "%.2f" %(round(total, 2))
		self.save()

