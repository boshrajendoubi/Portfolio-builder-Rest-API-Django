# Generated by Django 4.1.4 on 2022-12-15 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0003_alter_references_photo_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='references',
            name='Photo',
            field=models.ImageField(default='311872633_630546525429055_6007909932726738695_n.jpg', max_length=200, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Photo',
            field=models.ImageField(default='311872633_630546525429055_6007909932726738695_n.jpg', max_length=200, upload_to='photos/'),
        ),
    ]
