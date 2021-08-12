from django.urls import path
from .views import top_players, home, add_player, delete_player, edit_player

urlpatterns = [
    path('', top_players, name='top-players'),
    path('home/', home, name='home'),
    path('addplayer/', add_player, name='add-player'),
    path('editplayer/<int:pk>/', edit_player, name='edit-player'),

    path('deleteplayer/<int:pk>/', delete_player, name='delete-player'),




]
