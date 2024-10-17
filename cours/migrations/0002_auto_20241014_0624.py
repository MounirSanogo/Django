# Generated by Django 3.2.17 on 2024-10-14 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='etudiant',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.AddField(
            model_name='notification',
            name='cours',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='cours.cours'),
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_notifications', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.TextField(),
        ),
    ]
