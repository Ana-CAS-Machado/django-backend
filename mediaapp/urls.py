from django.urls import path, include
from .views import MediaItemListView, HomeMediaView, FormMediaView, ScheduleMediaView, SpeakersMediaView, StreamMediaView, ImageRetrieveView

urlpatterns = [
    path('', MediaItemListView.as_view(), name='media-list'),
    path('home/', HomeMediaView.as_view(), name='media-home'),
    path('form/', FormMediaView.as_view(), name='media-form'),
    path('schedule/', ScheduleMediaView.as_view(), name='media-schedule'),
    path('speakers/', SpeakersMediaView.as_view(), name='media-speakers'),
    path('stream/', StreamMediaView.as_view(), name='media-stream'),
    path('media/image/<int:image_id>/', ImageRetrieveView.as_view(), name='image-retrieve'),
]