from django.urls import path
from .views import SignUpView, SongCreate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('songs/', SongCreate.as_view(), name='songs'),
    
]