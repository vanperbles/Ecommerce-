# Generated by Django 2.2.7 on 2019-11-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0003_auto_20191118_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='image.jpg', upload_to='product_Images'),
        ),
    ]
