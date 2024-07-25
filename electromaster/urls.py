"""
URL configuration for electromaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carts/', include("carts.urls")),
    path('Electro/' , views.home , name='home'),
    path('track/' , views.track , name='track'),
    path('contact/' , views.contact , name='contact'),
    path('about/' , views.about , name='about'),
    path('privacy_policy/' , views.privacy_policy , name='privacy_policy'),
    path('terms_conditions/' , views.terms_conditions , name='terms_conditions'),
    path('payment_methods/' , views.payment_methods , name='payment_methods'),
    path('refunds_returns_policy/' , views.refunds_returns_policy , name='refunds_returns_policy'),
    path('shipping_delivery/' , views.shipping_delivery , name='shipping_delivery'),
    path('frequently_asked_questions/' , views.frequently_asked_questions , name='frequently_asked_questions'),
    path("wishlist/" , views.wishlist , name="wishlist"),
    path("compare/" , views.compare , name="compare"),

    path('store/' , include("store.urls")),
    path('accounts/', include("accounts.urls")),

] + static (settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
