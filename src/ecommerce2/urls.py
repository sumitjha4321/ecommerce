from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from carts.views import CartView, CartItemCount, CheckOutView
from orders.views import AddressFormView, UserAddressCreateView


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce2.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^today/$', 'today.views.home', name="todayhome"),
    url(r'^formset/$', 'today.views.formsetview', name = "formset"),
    url(r'^modelform/$', 'today.views.modelform', name = "modelform"),
    url(r'^modelformfactory/$', 'today.views.modelformfactory', name = "modelformfactory"),
    url(r'^categories/',  include('products.urls_categories')),
    url(r'^cart/$', CartView.as_view(), name = 'cartview'),
    url(r'^cart/count/$', CartItemCount.as_view(), name='cartcountview'),
    url(r'^checkout/$', CheckOutView.as_view(), name='checkout'),
    url(r'^checkout/address/$', AddressFormView.as_view(), name = 'order_address'),
    url(r'^checkout/address/add$', UserAddressCreateView.as_view(), name = 'create_address'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)