from django.urls import path
from . import views

urlpatterns = [
    #Render routes
    path('', views.index),
    path('success', views.success),

    #Action/Redirect routes
    path('login', views.login)
]