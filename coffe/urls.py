from unicodedata import name
from django.urls import path
from .views import coffee, desc
urlpatterns = [
    path('',coffee, name='index'),
    path('describe/',desc, name='index')
]
