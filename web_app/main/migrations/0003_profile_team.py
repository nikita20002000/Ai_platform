# Generated by Django 5.0.2 on 2024-03-16 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile'),
        ('to_do_list', '0007_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='to_do_list.project'),
        ),
    ]
