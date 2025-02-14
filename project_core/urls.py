"""
URL configuration for project_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
brand_name = '8 Sync Dev'
admin.site.site_header = f'{brand_name} Administration'
admin.site.site_title = f'{brand_name} Administration'
admin.site.name = f'{brand_name} Administration'
admin.site.index_title = f'Welcome to {brand_name} Administration' 

urlpatterns = [
    path('admin/', admin.site.urls),
]
