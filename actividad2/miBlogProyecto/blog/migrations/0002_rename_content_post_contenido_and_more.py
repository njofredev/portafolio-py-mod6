# Generated by Django 5.0.4 on 2024-04-23 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='Contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='FechaPost',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='TituloPost',
        ),
    ]
