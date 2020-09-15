from django.urls import path

from . import views

urlpatterns = [
    #path('', views.manager, name='manager'),
    path('<uuid:code>/', views.manager, name='manager'),
    path('<uuid:code>/<int:page>/', views.manager, name='session'),
    path("clear", views.clear, name = "clear")
]