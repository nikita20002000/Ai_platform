# Generated by Django 5.0.2 on 2024-03-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0003_alter_sell_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
