from django.urls import path
from . import views

app_name = 'Chat'

urlpatterns = [
    path("chat/", views.index, name="Chat"),
    path("chat/<str:room_name>/", views.room, name="Room"),
]