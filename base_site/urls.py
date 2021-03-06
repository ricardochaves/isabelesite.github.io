"""base_site URL Configuration

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

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from base_site.mainapp import views

urlpatterns = [
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("ricardo/", admin.site.urls),
    url(r"^$", views.index, name="index"),
    url(r"coaching/", views.coaching, name="coaching"),
    url(r"psicologia/", views.psicologia, name="psicologia"),
    path("healthcheck/", include("health_check.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
