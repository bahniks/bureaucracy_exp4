from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('<uuid:code>/', views.manager, name='manager'),
    path('<uuid:code>/<int:page>/', views.manager, name='session'),
    path('add_codes/<int:number>/', views.codes, name='add_codes'),
    path('delete_data/', views.delete, name='delete_data'),
    path("clear", views.clear, name = "clear"), # for testing
    path('participants/', views.showParticipants, name='show_participants'),
    path('participant_data/', views.showParticipantLinks, name='show_participants_links'),
    path('data/<uuid:code>/', views.showData, name='show_data'),
]