# Generated by Django 2.2 on 2022-07-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220719_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='AsientoRestantes',
            field=models.IntegerField(),
        ),
    ]