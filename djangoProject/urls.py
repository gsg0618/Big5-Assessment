"""
URL configuration for djangoProject project.

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
from django.urls import path
from Big5App import views
from Big5App.views import analysis_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path('store_name/', views.store_name, name='store_name'),
    path('assessment/', views.assessment, name='assessment'),
    #path('assessment2/', views.assessment2, name='assessment2'),
    #path('assessment3/', views.assessment3, name='assessment3'),
    #path('assessment4/', views.assessment4, name='assessment4'),
    #path('assessment5/', views.assessment5, name='assessment5'),
    path('success/', views.success, name='success'),
    path('analysis/', views.analysis_view, name='analysis'),

]
