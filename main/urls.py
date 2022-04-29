from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("books/", AllBookView.as_view()),
    path("books/<int:pk>/", OneBookView.as_view()),
    path("audio/books/",AllAudioBookView.as_view()),
    path("rating/audio/add/<int:pk>/",RatingAudioBookAddView.as_view()),
]