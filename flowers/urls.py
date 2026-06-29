from django.urls import path

from flowers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contacts/', views.contacts, name='contact'),
]