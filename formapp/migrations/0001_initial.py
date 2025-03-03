# Generated by Django 5.1.5 on 2025-01-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('comprovante', models.FileField(upload_to='comprovantes/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
