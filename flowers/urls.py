from django.urls import path

from flowers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('addpage/', views.add_page, name='add_page'),
    path('contacts/', views.contacts, name='contact'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('search/', views.flower_search, name='search'),
]