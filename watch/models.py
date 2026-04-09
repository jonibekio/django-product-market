from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    sotuvchi = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50)
    warranty_months = models.PositiveIntegerField(default=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/%Y/%m/%d/")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        db_table = "product_images"
        verbose_name = "Mahsulot rasmi"
        verbose_name_plural = "Mahsulot rasmlari"
