from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    products = models.ForeignKey('Board', on_delete=models.DO_NOTHING, verbose_name='Товары', blank=True, null=True)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=255)

    def __str__(self):
        return str(self.name)

class Board(models.Model):
    STATUS = [
        ('А', 'Активен'),
        ('Н', 'Неактивен'),
    ]

    title = models.CharField(verbose_name="Название объявления", max_length=255, blank=False, null=False)
    price = models.IntegerField(verbose_name="Цена", blank=True, null=True)
    image = models.ImageField(verbose_name="Фотография", upload_to='static/image',blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=255, blank=True, null=True)
    email = models.CharField(verbose_name="Email", max_length=254, blank=True, null=True)
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория', blank=True, null=True)
    status = models.CharField(verbose_name="Статус товара", max_length=255, blank=True, null=True, choices=STATUS)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True, max_length=255)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('board', kwargs={'board_slug': self.slug})
    
    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"

    
