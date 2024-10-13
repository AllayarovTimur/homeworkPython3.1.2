from django.db import models
from django.db.models import IntegerField


# Create your models here.
class Products(models.Model):
    pId = models.IntegerField(verbose_name="ID продукта")
    pName = models.CharField(verbose_name="Название", max_length=40)
    pDate = models.DateField(verbose_name="Дата публикации товара", auto_now=False)
    pCount = models.IntegerField(verbose_name="Количество товара")
    pPhoto = models.ImageField(verbose_name="Фото", null=True)

    pCategory = models.ForeignKey(
        'Categories',
        verbose_name="Категория",
        max_length=30,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = 'Продукты',
        ordering = ['pId']

    def __str__(self):
        return f'{self.pName}'

class Categories(models.Model):
    cId = models.IntegerField(verbose_name="ID категории")
    cChoices = [
        ('Food', 'Еда'),
        ('Clothes','Одежда'),
        ('HApp','Бытовая техника'),
        ('Services','Услуги'),
    ]
    cName = models.CharField(verbose_name="Категория", max_length=8, choices=cChoices, default="-")

    class Meta:
        verbose_name = "Категория",
        verbose_name_plural = "Категории",
        ordering = ['cId']

    def __str__(self):
        return self.cName

class Shops(models.Model):
    sId = IntegerField(verbose_name="ID магазина")
    sName = models.CharField(verbose_name="Магазин",max_length=40,)
    sPrice = models.IntegerField(verbose_name="Цена")
    pId = models.ManyToManyField(
        Products,
        verbose_name="ID продукта",
        max_length=40
    )
    class Meta:
        verbose_name = 'Магазин',
        ordering = ['sId']

    def __str__(self):
        return f'{self.sName}'

    def getPriceWithDiscount(self):
        return 0.9*self.sPrice

class Customers(models.Model):
    custId = models.IntegerField(verbose_name="ID покупателя")
    custName = models.CharField(verbose_name="Покупатель", max_length=40)
    sId = models.ManyToManyField(
        Shops,
        verbose_name="ID Магазина",
        max_length=40
    )
    pId = models.ManyToManyField(
        Products,
        verbose_name = "ID Товара",
        max_length = 40
    )

    class Meta:
        verbose_name = "Покупатель",
        verbose_name_plural = "Покупатели",
        ordering = ['custId']

    def __str__(self):
        return self.custName