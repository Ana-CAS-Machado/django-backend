from django.db import models

# Create your models here.

class MediaItem(models.Model):
    CATEGORY_CHOICES = [
        ('home', 'Página Inicial'),
        ('form', 'Formulário'),
        ('schedule', 'Programação'),
        ('speakers', 'Palestrantes'),
        ('stream', 'Transmissão'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
