"""
URL configuration for Health_Evaluation_App project.

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
from django.urls import path
from django.urls import include
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User)
admin.site.register(User, UserAdmin)

admin.site.site_header = "Health Evaluation Admin"
admin.site.site_title = "Health Evaluation Admin Portal"
admin.site.index_title = "Welcome to Health Evaluation Data Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webapp.urls')),

]
