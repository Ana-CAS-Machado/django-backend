from rest_framework import serializers
from .models import HomePage, Video, Speaker, Schedule, Event

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['horario', 'eixo', 'mesa', 'componente']

class ScheduleSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Schedule
        fields = ['date', 'events']
