# Generated by Django 2.2.7 on 2019-11-16 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterit', '0010_auto_20191116_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject2',
            name='your_name',
            field=models.CharField(default='{user.username}', max_length=100),
        ),
    ]
