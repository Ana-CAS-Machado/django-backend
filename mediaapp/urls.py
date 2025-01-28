from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomePageViewSet, VideoViewSet, SpeakerViewSet, ScheduleViewSet

# Configuração do roteador com as ViewSets
router = DefaultRouter()
router.register(r'home', HomePageViewSet, basename='home-page')
router.register(r'videos', VideoViewSet, basename='video-list')
router.register(r'speakers', SpeakerViewSet, basename='speaker-list')
router.register(r'schedules', ScheduleViewSet, basename='schedule-list')

# Incluindo as rotas do roteador
urlpatterns = [
    path('', include(router.urls)),
]
