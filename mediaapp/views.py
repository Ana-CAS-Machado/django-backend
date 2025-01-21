from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomePage, Video, Speaker, Schedule
from .serializers import HomePageSerializer, VideoSerializer, SpeakerSerializer, ScheduleSerializer

class HomePageView(APIView):
    def get(self, request):
        homepage_data = HomePage.objects.all()
        serializer = HomePageSerializer(homepage_data, many=True)
        return Response(serializer.data)

class VideoView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class SpeakerView(APIView):
    def get(self, request):
        speakers = Speaker.objects.all()
        serializer = SpeakerSerializer(speakers, many=True)
        return Response(serializer.data)

class ScheduleView(APIView):
    def get(self, request):
        schedules = Schedule.objects.prefetch_related('events').all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
