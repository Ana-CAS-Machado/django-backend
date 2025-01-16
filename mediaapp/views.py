from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MediaItem
from .serializers import MediaItemSerializer
import os


class ImageRetrieveView(APIView):
    def get(self, request, *args, **kwargs):
        image_id = kwargs.get('image_id')
        media_item = MediaItem.objects.get(id=image_id)
        
        file_path = media_item.file.path
        return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')  # Ajuste conforme o tipo de imagem


        
class MediaItemListView(APIView):
    def get(self, request, category=None):
        if category:
            items = MediaItem.objects.filter(category=category)
        else:
            items = MediaItem.objects.all()
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)


class HomeMediaView(APIView):
    def get(self, request, *args, **kwargs):
        items = MediaItem.objects.filter(category='home')
        data = [{"id": item.id, "title": item.title, "description": item.description, "file": item.file.url if item.file else None, "link": item.link} for item in items]
        return Response(data)

class FormMediaView(APIView):
    def get(self, request):
        items = MediaItem.objects.filter(category='form')
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

class ScheduleMediaView(APIView):
    def get(self, request):
        items = MediaItem.objects.filter(category='schedule')
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

class SpeakersMediaView(APIView):
    def get(self, request):
        items = MediaItem.objects.filter(category='speakers')
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)

class StreamMediaView(APIView):
    def get(self, request):
        items = MediaItem.objects.filter(category='stream')
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)