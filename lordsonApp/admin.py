from django import forms
from django.contrib import admin
from openpyxl import Workbook
from django.http import HttpResponse
import datetime
import json
from lordsonApp.models import Banner, Product, ProductImage





@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')



class ProductForm(forms.ModelForm):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', '2X Large'),
    ]

    sizes = forms.MultipleChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Product
        fields = '__all__'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('title', 'category', 'price', 'discount', 'final_price', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    readonly_fields = ('final_price',)
    inlines = [ProductImageInline]

