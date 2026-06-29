from django.urls import path

from flowers import views

urlpatterns = [
    path('', views.index, name='index'),
]