# Generated by Django 5.0.2 on 2024-03-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0010_remove_project_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_color',
            field=models.CharField(choices=[('Системный', 'Системный'), ('Синий', 'Зеленый'), ('Голубой', 'Голубой'), ('Желтый', 'Желтый'), ('Оранжевый', 'Оранжевый')], default='Системный', max_length=20),
        ),
    ]