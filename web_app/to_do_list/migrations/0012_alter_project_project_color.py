# Generated by Django 5.0.2 on 2024-03-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0011_project_project_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_color',
            field=models.CharField(choices=[('COLOR_SYSTEM', 'Системный'), ('COLOR_CHOICE_DEEP_BLUE', 'Синий'), ('COLOR_CHOICE_BLUE', 'Голубой'), ('COLOR_CHOICE_GREEN', 'Зеленый'), ('COLOR_CHOICE_LIGHT_YELLOW', 'Желтый'), ('COLOR_CHOICE_ORANGE', 'Оранжевый')], default='COLOR_SYSTEM', max_length=40),
        ),
    ]
