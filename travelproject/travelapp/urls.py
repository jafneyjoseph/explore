from .   import views
from django.urls import path

urlpatterns = [

    # path('places/', views.places, name='places'),
    # path('teams/', views.teams, name='teams'),
    path('', views.places, name='places'),
    path('teams/', views.teams, name='teams'),

]