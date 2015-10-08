from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.main_page, name='main_page'),
   url(r'^system_feature/', views.system_feature, name='system_feature'),
   url(r'^about_us/', views.about_us, name='about_us'),
   url(r'^system/', views.system, name='system'),
   url(r'^issues/', views.issues, name='issues'),
   url(r'^contact/', views.contact, name='contact'),
   url(r'^feedback/', views.feedback, name='feedback'),
]