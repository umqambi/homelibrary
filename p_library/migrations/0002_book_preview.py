# Generated by Django 2.2.7 on 2019-11-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preview',
            field=models.ImageField(blank=True, upload_to='books_prewies/%Y/%m/%d'),
        ),
    ]
