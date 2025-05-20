from rest_framework import serializers
from .models import Product, ProductImage, ProductColor, Brand, Feature

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['color_name', 'hex_code', 'extra_price']

class ProductSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'base_price', 'colors']

    def get_colors(self, obj):
        if obj.colors.exists():
            return ProductColorSerializer(obj.colors.all(), many=True).data
        return None  # یا می‌تونی [] برگردونی بسته به فرانتت



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'logo']
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'key', 'value', 'is_main_feature']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True)
    features = FeatureSerializer(many=True, read_only=True)  # ✅ اینجا سریالایزر کامل

    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description',
            'base_price', 'brand', 'images', 'colors', 'features'
        ]

# serializers.py
