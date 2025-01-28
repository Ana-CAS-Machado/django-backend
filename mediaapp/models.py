from django.db import models

class HomePage(models.Model):
    img_home = models.URLField()
    data = models.CharField(max_length=100)
    local = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    strong_data = models.CharField(max_length=50)
    strong_local = models.CharField(max_length=50)
    txt_1 = models.TextField()
    txt_2 = models.TextField()
    txt_3 = models.TextField()

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    type = models.CharField(max_length=50)

class Speaker(models.Model):
    img = models.URLField(blank=True, null=True)
    title2 = models.CharField(max_length=100)
    title4 = models.CharField(max_length=100)
    title5 = models.CharField(max_length=100)
    description = models.TextField()

class Schedule(models.Model):
    date = models.CharField(max_length=50)

class Event(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='events', on_delete=models.CASCADE)
    horario = models.CharField(max_length=50)
    eixo = models.CharField(max_length=255)
    mesa = models.TextField(blank=True, null=True)
    componente = models.CharField(max_length=255, blank=True, null=True)
