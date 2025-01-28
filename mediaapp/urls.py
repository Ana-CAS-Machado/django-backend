from django.urls import path
from .views import HomePageView, VideoView, SpeakerView, ScheduleView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home-page'),
    path('videos/', VideoView.as_view(), name='video-list'),
    path('speakers/', SpeakerView.as_view(), name='speaker-list'),
    path('schedule/', ScheduleView.as_view(), name='schedule-list'),
]
