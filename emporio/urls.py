"""emporio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import include, re_path
#from django.http import HttpResponse, HttpResponseRedirect
# from products.views import (ProductListView, 
#                             product_list_view, 
#                             ProductDetailView, 
#                             product_detail_view,
#                             ProductDetailSlugView,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView)
from .views import (home_page,
                    about_page,
                    contact_page,
                    login_page,
                    register_page)

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
	path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('products/', include("products.urls")),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view),
    # path('products/<int:pk>', ProductDetailView.as_view()),
    # path('products-fbv/<int:pk>', product_detail_view),
    # path('products/<slug:slug>/', ProductDetailSlugView.as_view()),    
    re_path(r'^favicon\.ico$', favicon_view),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
