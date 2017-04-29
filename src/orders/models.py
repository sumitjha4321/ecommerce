from decimal import Decimal

from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

from carts.models import Cart



class UserCheckOut(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)
	email = models.EmailField(unique=True)

	def __unicode__(self):
		return self.email

address_type = (
	('billing' , 'Billing'),
	('shipping', 'Shipping'),

)
class UserAddress(models.Model):
	user = models.ForeignKey(UserCheckOut)
	type = models.CharField(max_length=120, choices=address_type)
	name = models.CharField(max_length = 120)
	mobile = models.CharField(max_length = 120)
	address1 = models.CharField(max_length = 120,)
	address2 = models.CharField(max_length = 120, blank=True, null=True, )
	pin = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)

	def __unicode__(self):
		return self.user.email + "  (" + self.type + ")"


	def get_address(self):
		return "%s, %s - %s" %(self.address1 + self.address2, self.state, self.pin )


class Order(models.Model):
	cart = models.ForeignKey(Cart)
	user = models.ForeignKey(UserCheckOut, null=True)
	billing_address = models.ForeignKey(UserAddress, related_name = "billing_address", null=True)
	shipping_address = models.ForeignKey(UserAddress, related_name = "shipping_address", null=True)
	shipping_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

	def __unicode__(self):
		return str(self.cart.id)



def order_total_presave(sender, instance, *args, **kwargs):
	instance.order_total = Decimal(instance.shipping_total_price) + Decimal(instance.cart.total)





pre_save.connect(order_total_presave, sender=Order)