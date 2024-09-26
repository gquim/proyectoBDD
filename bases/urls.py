from django.urls import path
#importa el HOME de las rutas
from bases.views import Home
urlpatterns = [
    #ingreso de ruta como vista, con nombre home
    path('',Home.as_view(),name='home'),
]