# Generated by Django 4.0 on 2022-10-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0005_post_is_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
