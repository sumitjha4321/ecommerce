from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView, ProductListView, VariationListView, CategoriesListView, CategoriesDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    
    
    url(r'^$', CategoriesListView.as_view(), name="CategoriesListView"),
    url(r'^(?P<slug>[\w-]+)/$', CategoriesDetailView.as_view(), name="CategoriesDetailView"),


 
]