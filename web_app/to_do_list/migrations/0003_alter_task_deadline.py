# Generated by Django 5.0.2 on 2024-03-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_task_deadline_task_executor_task_project_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]