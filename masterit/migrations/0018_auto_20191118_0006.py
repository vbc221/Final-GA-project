# Generated by Django 2.2.7 on 2019-11-18 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterit', '0017_auto_20191118_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='author',
        ),
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.ForeignKey(default='your name', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
