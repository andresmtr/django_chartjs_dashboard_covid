
from django.conf.urls import url 
from .views import Inicio
from base import views
from django.urls import path

urlpatterns = [
    # url('',views.index, name = 'index'),
    # url('',views.index, name = 'index'),
    # path('hello/', myView),
    path('',Inicio, name = 'index'),
]
