from django.contrib import admin
from django.urls import path
from webapp import views


urlpatterns = [
   path("",views.login_view, name='login'),
   path('registration/',views.registration_page, name='registration'),
   path('index/',views.index,name='home'),
   path("user_form/",views.user_form, name='user_form'),
   path("about_us/",views.about_us,name='about_us'),
   path("doctor_ai/",views.doctor_ai,name='doctor_ai'),
   path("logout/",views.logout_view,name='logout'),
]

