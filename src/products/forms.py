from django import forms
from django.forms import modelformset_factory, BaseModelFormSet


from .models import Variation, ProductImage, ProductFeatured, Comment


class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = [
			"title",
			"price", 
			"sale_price", 
			"inventory",
			"active"
		]
class BaseVariationInventoryFormSet(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		super(BaseVariationInventoryFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted=False
		#self.queryset = Variation.objects.all()

		

VariationInventoryFormSet = modelformset_factory(Variation, form = VariationInventoryForm, formset=BaseVariationInventoryFormSet, extra=1)
	
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['product']

class BaseCommentFormSet(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		super(BaseCommentFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted=False

CommentFormSet = modelformset_factory(Comment, form = CommentForm, formset = BaseCommentFormSet)