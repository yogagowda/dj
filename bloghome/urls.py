from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ublog', views.blog, name='blog'),
    path('ublogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('ucontact', views.contact, name='contact'),
    path('usearch', views.search, name='search')


]