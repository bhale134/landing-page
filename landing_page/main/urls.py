from .views import *
from django.urls import path

urlpatterns =[
    path("",index,name='index'),
    path("plan/",plan,name='plan'),
    path("templates/",template,name='templates'),
    path("register/",register,name='register'),
    path("final/",final_page,name='final')
]