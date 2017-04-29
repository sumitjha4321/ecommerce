from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils.safestring import mark_safe


class ProductManager(models.Manager):
	def get_queryset(self):  # note 'get_queryset' and 'all' method is same !!
		return super(ProductManager, self).get_queryset()

	def show_disabled_products(self):
		return super(ProductManager, self).get_queryset().filter(active=False)

	def get_related(self, instance):
		
		
		qs1 =  self.get_queryset().filter(categories=instance.categories.all())
				#instance.categories.all() will give all the categories to which this instance belongs..
				#...NOT ALL THE AVAILABLE CATEGORIES !!
		qs2 = self.get_queryset().filter(default = instance.default)
		qs = (qs1 | qs2).exclude(id=instance.id).distinct()
		return qs



	
class ProductQuerySet(models.QuerySet):
	def show_only_active_product(self):
		return self.filter(active=True)

	def show_only_passive_product(self):
		return self.filter(active=False)



class Product(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20)
	active = models.BooleanField()
	categories = models.ManyToManyField('Category', blank=True)
	default = models.ForeignKey('Category', related_name = 'default_category', null=True, blank = True)

	objects = ProductManager()
	custom = ProductQuerySet.as_manager()
	

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('ProductDetailView', kwargs = {'pk':self.pk})

	def get_absolute_url_variation(self):
		return reverse('VariationListView', kwargs = {'pk' : self.id})

	def get_image_url(self):
		img = self.productimage_set.first()
		if img:
			return img.image.url

		return img #None





class Variation(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length = 120)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	sale_price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
	inventory = models.IntegerField(default = -1)
	active = models.BooleanField()

	def __unicode__(self):
		return self.title + " (" + self.product.title + ")"

	def get_price_html(self):
		if self.sale_price:
			html_text="<span class='sale-price'>%s</span> <span class='og-price'>%s</span>"%(self.sale_price, self.price)

		else:
			html_text="<span class='price'>%s</span>"%(self.price)
		return mark_safe(html_text)

	def remove_from_cart(self):
		return "%s?item_id=%s&delete=True"%(reverse('cartview'), self.id)

	def get_price(self):
		if self.sale_price:
			return self.sale_price
		else:
			return self.price



def product_image_upload(instance, filename):
	#instance is the __unicode__ of the ProductImage
	#filename is the name of the file being uploaded


	slug = slugify(instance) 
	file_extension = filename.split(".")[1]
	return "products/%s.%s"%(slug, file_extension)


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.FileField(upload_to=product_image_upload)

	def __unicode__(self):
		return self.product.title

class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(unique = True)
	description = models.TextField(blank=True, null=True)
	active = models.BooleanField(default = True)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	class Meta:
		verbose_name_plural = "Category"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("CategoriesDetailView", kwargs = {'slug': self.slug})


def product_featured_image_upload(instance, filename):
	#instance is the __unicode__ of the ProductImage
	#filename is the name of the file being uploaded
	
	slug = slugify(instance) 
	#print "slug is: ", slug
	file_extension = filename.split(".")[1]
	#print "products/%s/featured.%s"%(slug, file_extension)
	return "products/featured/%s.%s"%(slug, file_extension)


class ProductFeatured(models.Model):
	product = models.ForeignKey(Product)
	image = models.FileField(upload_to = product_featured_image_upload)
	title = models.CharField(max_length=120, null=True, blank=True)
	text = models.CharField(max_length=220, null=True, blank=True)
	text_right = models.BooleanField(default=False)
	show_price = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	make_background_image = models.BooleanField(default=False)

	def __unicode__(self):
		return self.product.title






class CommentManager(models.Manager):
	def get_comment(self, instance_id, *args, **kwargs):
		
		return self.get_queryset().filter(product__id=instance_id)

class Comment(models.Model):
	product = models.ForeignKey(Product, null=True, blank=True)
	# product2 = models.ForeignKey(Product, null=True, blank=True)
	username = models.CharField(max_length=20, null=True, blank=True)
	rating = models.DecimalField(decimal_places=1, max_digits=3, null=True, blank=True)
	subject = models.CharField(max_length=120, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

	objects = CommentManager()

	def __unicode__(self):
		return self.product.title

	
	




def product_post_save_receiver(sender, instance, created, *args, **kwargs):
	product = instance
	variations = product.variation_set.all()
	if variations.count() == 0:
		# Do this 
		new_var = Variation()
		new_var.product = product
		new_var.title = "Default for "+product.title 
		new_var.price = product.price
		new_var.active = True
		new_var.save()
		# or simply, do:
		# product.variation_set.create(title="Default for "+product.title, price=product.price, active=product.active)



post_save.connect(product_post_save_receiver, sender=Product)






