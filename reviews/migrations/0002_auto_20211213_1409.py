# Generated by Django 3.2.7 on 2021-12-13 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['date_added']},
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='posting_date',
            new_name='date_added',
        ),
    ]
