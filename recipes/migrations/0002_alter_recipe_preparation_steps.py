# Generated by Django 4.1 on 2022-09-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(),
        ),
    ]
