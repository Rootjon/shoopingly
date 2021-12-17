from django.contrib import admin
from .models import(
    Customer,
    Product,
    Cart,
    Orderplace
)

@admin.register(Customer)
class CustomerModeladmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user',
        'name',
        'locality',
        'city',
        'zipcode',
        'district',    
    ]


@admin.register(Product)
class ProductModeladmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
        'selling_price',
        'discount_price',
        'description',
        'brand',
        'category',
        'product_image',    
    ]



@admin.register(Cart)
class CartModeladmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user',
        'product',
        'quantity',
           
    ]


@admin.register(Orderplace)
class OrderplaceModeladmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user',
        'customer',
        'quantity',
        'ordered_date',
        'status',
        'product',    
    ]
