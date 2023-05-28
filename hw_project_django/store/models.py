from django.db import models

class Product(models.Model):
    CHOICES = (
        ('new', 'Новый'),
        ('sale', 'Распродажа'),
        ('promo', 'Промо'),
    )

    title = models.CharField(max_length=100, default='Untitled')
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', default='default_image.jpg')
    choose = models.CharField(max_length=10, choices=CHOICES, default='new')
