# Generated by Django 2.1.2 on 2018-10-25 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emial',
            new_name='email',
        ),
    ]
