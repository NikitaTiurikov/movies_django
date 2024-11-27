from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('picture/<int:pict_id>/', views.selected_picture, name='picture'),
    path('<str:cat>/', views.selected_type, name='type'),
    path('<str:cat>/<str:genre>/', views.selected_genre, name='genre'),
]
