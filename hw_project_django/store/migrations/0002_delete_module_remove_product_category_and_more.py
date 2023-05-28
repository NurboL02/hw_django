# Generated by Django 4.2.1 on 2023-05-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='choose',
            field=models.CharField(choices=[('new', 'Новый'), ('sale', 'Распродажа'), ('promo', 'Промо')], default='new', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]