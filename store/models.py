from django.db import models

# --- دسته‌بندی ---
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True) 
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name


# --- برند ---
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name

class Feature(models.Model):
   
    key = models.CharField(max_length=255, verbose_name='نام ویژگی')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی')
    is_main_feature = models.BooleanField(default=False, verbose_name='ویژگی اصلی')

    def __str__(self):
        try:
            product_name = self.product.name
        except:
            product_name = "محصول تعریف‌نشده"
        status = 'ویژگی اصلی' if self.is_main_feature else 'ویژگی عمومی'
        return f"{product_name} | {self.key} = {self.value} ({status})"

# --- محصول ---
class Product(models.Model):
    features = models.ManyToManyField(Feature, related_name='products', blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    base_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# --- ویژگی (کلی یا فنی) ---
# class Feature(models.Model):
#     FEATURE_TYPES = (
#         ('general', 'اطلاعات کلی'),
#         ('technical', 'مشخصات فنی'),
#     )
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=10, choices=FEATURE_TYPES)

#     def __str__(self):
#         return f"{self.get_type_display()} - {self.name}"


# --- مقدار ویژگی برای محصول ---


# --- گالری تصاویر ---
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"


# --- رنگ با تاثیر اختیاری در قیمت ---
class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    color_name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.color_name} for {self.product.name}"
