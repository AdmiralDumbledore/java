from django.urls import path
from .views import *

app_name = "messenger"

urlpatterns = [
    path('message/', SendMessage.as_view()),
    path('message_confirmation/', SetStatus.as_view()),
]
