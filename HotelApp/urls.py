"""HotelApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

app_name = 'HotelApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('managementApp/',include('ManagementApp.urls')),
    path('',views.homepage),
    path('services/',views.services),
    path('aboutus/',views.aboutus),
    path('fitness/',views.fitness),
    path('hotelrooms/',views.hotelrooms),
    path('contactus/',views.contactus),
    path('restroBar/',views.restroBar),
    path('checkavail/',views.checkavail),
    path('roombooking/<int:id>/',views.roombooking,name='roombooking'),
    path('HRpayment/',views.HRpayment),
    path('orderfood/',views.orderfood),
    path('orderdrink/',views.orderdrink),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
