from .   import views
from django.urls import path

urlpatterns = [

    path('', views.places, name='places'),

]