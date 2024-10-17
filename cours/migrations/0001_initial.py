# Generated by Django 3.2.17 on 2024-09-28 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuteurs', '0001_initial'),
        ('etudiants', '0002_auto_20240928_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='cours_pdfs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('etudiant', models.ManyToManyField(blank=True, related_name='cours', to='etudiants.Etudiantinscrip')),
                ('tuteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cours', to='tuteurs.tuteurinscrip')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='cours.cours')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='cours.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
