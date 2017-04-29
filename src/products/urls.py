from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView, ProductListView, VariationListView, CategoriesListView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    
    url(r'^$', ProductListView.as_view(), name = "ProductListView"),
    url(r'^(?P<pk>[0-9]+)/$', ProductDetailView.as_view(), name="ProductDetailView"),
    url(r'^(?P<pk>[0-9]+)/inventory/$', VariationListView.as_view(), name="VariationListView"),
    



 
]