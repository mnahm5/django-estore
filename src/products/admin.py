from django.contrib import admin

# Register your models here.

from .models import Product, Variation, ProductImage, Category, ProductFeatured

class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0
    max = 10

class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 0
    max = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'price']
    inlines = [
        ProductImageInLine,
        VariationInLine,
    ]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

#admin.site.register(Variation)

#admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)