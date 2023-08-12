from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Название",max_length=50)
    slug = models.SlugField("Слак", max_length=70)
    parent = models.ForeignKey(
        "self", 
        on_delete=models.PROTECT, 
        related_name="subcategories",
        null=True,
        blank=True
    )

    class Meta: 
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name
    



class Product(models.Model):
    title = models.CharField("Название", max_length=300)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="products"
        )
    
    stock_count = models.PositiveIntegerField("Количество на складе")
    created_at = models.DateTimeField("Создано",auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)


    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"
        ordering = ["-created_at"]

    
    def __str__(self):
        return self.title
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pics")
    image = models.ImageField("Изображение",upload_to="products/images/")    
    is_main = models.BooleanField("Главное фото", default=False)
    