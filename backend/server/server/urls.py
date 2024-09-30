"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from app.views import EndpointViewSet, MLModelViewSet, MLModelStatusViewSet, MLRequestViewSet

# Initialize the DRF router
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlmodels", MLModelViewSet, basename="mlmodels")
router.register(r"mlmodelstatuses", MLModelStatusViewSet, basename="mlmodelstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

# Define the URL patterns
urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),  # Use re_path for regex-based URLs
    path('admin/', admin.site.urls),  # Use path for simple non-regex URLs
]

