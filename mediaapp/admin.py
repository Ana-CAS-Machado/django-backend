from django.contrib import admin

# Register your models here.
from .models import HomePage, Video, Speaker, Schedule, Event

admin.site.register(HomePage)
admin.site.register(Video)
admin.site.register(Speaker)
admin.site.register(Schedule)
admin.site.register(Event)