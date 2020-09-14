from django.urls import path

from . import views

urlpatterns = [
    #path('', views.manager, name='manager'),
    path('<uuid:code>/', views.manager, name='manager'),
    path("clear", views.clear, name = "clear")
]