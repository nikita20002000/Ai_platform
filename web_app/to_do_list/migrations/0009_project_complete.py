# Generated by Django 5.0.2 on 2024-03-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0008_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
