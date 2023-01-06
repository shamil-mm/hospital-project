from django.urls import path
from . import views
urlpatterns = [path('', views.home, name="home"),
               path('about', views.about, name="about"),
               path('booking',views.booking , name='booking'),
               path('contact',views.contact, name='contact'),
               path('depart',views.depart, name='depart'),
               path('doctors',views.doct, name='doctors'),
               path('login',views.login,name="login"),

               ]