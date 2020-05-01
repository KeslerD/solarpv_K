from django.urls import path

from . import views

# Create your tests here.
urlpatterns = [path('', views.index, name='index'),path('registration/',views.registration,name='registration'),path('login/',views.login,name='login')]