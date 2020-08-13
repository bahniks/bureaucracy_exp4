from django.urls import path

from experiment.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='intro'),
]