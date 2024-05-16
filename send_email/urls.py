from django.urls import path
#internall
from .views import  home_page

urlpatterns=[
path("" ,home_page ,name="home" )
]