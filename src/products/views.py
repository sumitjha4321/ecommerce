from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import  Q
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.contrib import messages

from .models import Product, Variation, Category, Comment
from .forms import VariationInventoryFormSet, CommentFormSet
from .mixins import StaffRequiredMixin

class ProductDetailView(generic.DetailView):
	model = Product

	def my_queryset(self, instance_id): #queryset for 'CommentFormSet' in context["new-comment-form"] 
		#return Comment.objects.filter(product__id=instance_id)
		return Comment.objects.none()

	
	

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		

		context["related"] = Product.objects.get_related(instance).order_by("?")[:6]
		instance_id = instance.id
		context["comments"] = Comment.objects.get_comment(instance_id)
		context["new_comment_form"] = CommentFormSet(queryset = self.my_queryset(instance_id))

		return context

	def post(self, request, *args, **kwargs):

		formset = CommentFormSet(request.POST, request.FILES)
		product_id = self.kwargs.get("pk")
		product = get_object_or_404(Product, pk=product_id)
		
		if formset.is_valid():
			forms = formset.save(commit=False)
			for form in forms:
				form.product = product
				
				form.save()
			messages.success(request, "Your inventory has been updated.")
				

			return redirect("ProductListView")
		else:
			print self.kwargs
			#context = self.get_context_data()
			product_id = self.kwargs.get("pk")
			product = get_object_or_404(Product, pk=product_id)
			context = {
				"product" : product,
			}
			context["new_comment_form"] = formset
			context["formset_error"] = "Please rectify the errors shown below."
			return render(request, "product_detail.html", context)





class ProductListView(generic.ListView):

	model = Product
	def get_queryset(self):
		qs = super(ProductListView, self).get_queryset() #model=Product must be present for this to work !!
		 	 # OR DO THIS:    Product.objects.all()
		qs2 = super(ProductListView, self).get_queryset()
		query = self.request.GET.get("q") # the search bar in navbar.html has "name=q"
		if query:

			qs = self.model.objects.filter(
					Q(title__icontains=query) |
					Q(description__icontains=query) |
					Q(price__icontains=query)
				)
			# MERGING QUERY SET EXAMPLE
			try:
				qs2 = self.model.objects.filter(   #YOU MIGHT WANT TO PUT THIS IN TRY-CATCH BLOCK 
						Q(price__icontains=query)
				)
			except:
				pass
		return (qs | qs2 ).distinct()

	def get_context_data(self, *args, **kwargs):

		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context["now"] = timezone.now()
		context["sumit"] = Product.custom.show_only_active_product() #from ProductQuerySet
		context["amit"] = Product.objects.show_disabled_products()   #from ProductManager 
		return context


class VariationListView(StaffRequiredMixin, generic.ListView):
	model = Variation # since the model is 'variation', the 'get_context_data' which is one of the...
					  # ...'context' is named as 'variation_list', or 'object_list' (NOT OBJECTS_LIST) !! 

	def get_queryset(self, *args, **kwargs):
		print "args is:", args
		print "kwargs is:", kwargs
		print self.model



		
		
		#qs = super(VariationListView, self).get_queryset() #model=Variation must be present for this to work !!
														   #...this gives you 'Variation.objects.all()'
		
		product_id = self.kwargs.get("pk")
		product = get_object_or_404(Product, pk=product_id)
		qs = Variation.objects.filter(product=product)

		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(VariationListView, self).get_context_data(*args, **kwargs)
		context['formset_variation'] = VariationInventoryFormSet(queryset=self.get_queryset())#note that the queryset..
						#...which is passed into the function could have been defined inside the ...
						#...__init__ method of BaseVariationInventoryFormSet (the 'formset' attribute for...
						#...the modelformset_factory method while defining the 'VariationInventoryFormSet' in forms.py)..
						#...but since we didn't have access to 'pk' inside that, so we defined it here only.
						#Just to remind that both is permissible
						#Either 

		#context["product"] = self.product
		product_id = self.kwargs.get("pk")
		product = get_object_or_404(Product, pk=product_id)
		context["product"] = product

		return context

	def post(self, request, *args, **kwargs):

		formset = VariationInventoryFormSet(request.POST, request.FILES)
		product_id = self.kwargs.get("pk")
		product = get_object_or_404(Product, pk=product_id)
		
		if formset.is_valid():
			forms = formset.save(commit=False)
			for form in forms:
				form.product = product
				
				form.save()
			messages.success(request, "Your inventory has been updated.")
				

			return redirect("ProductListView")
		else:
			print self.kwargs
			#context = self.get_context_data()
			product_id = self.kwargs.get("pk")
			product = get_object_or_404(Product, pk=product_id)
			context = {
				"product" : product,
			}
			context["formset_variation"] = formset
			context["formset_error"] = "Please rectify the errors shown below."
			return render(request, "variation_list.html", context)


class CategoriesListView(generic.ListView):
	model = Category

	def get_queryset(self):
		return Category.objects.all()

class CategoriesDetailView(generic.DetailView):
	model = Category

		

	