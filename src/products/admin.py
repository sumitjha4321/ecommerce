from django.contrib import admin

from .models import Product, Variation, ProductImage, Category, ProductFeatured, Comment


class ProductFeaturedInline(admin.TabularInline):
	model = ProductFeatured
	extra = 1

class ProductImageInline(admin.TabularInline):
	model = ProductImage
	extra = 1

class VariationInline(admin.TabularInline):
	model = Variation
	extra = 1

class ProductAdmin(admin.ModelAdmin):
	inlines = [VariationInline, ProductImageInline, ProductFeaturedInline]
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(ProductFeatured)
admin.site.register(Comment)
