from django.contrib import admin

from . models import Product, Collection
from django.db.models.aggregates import Count
from django.db.models import F
# here we can give more fields in our admin panel and we can edit in the list all the products


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'collection',
                    'quantity', 'quantity_status']
    list_editable = ['collection']
    ordering = ['name']

    # we can give search_fields in it for search products here we can give lookups also
    search_fields = ['name__istartswith']

    # we can add filters for showing our products with filter
    list_filter = ['name', 'price', 'collection']


# we can give extra field in our admin list for showig status of our products and anything else

    def quantity_status(self, Product):
        if Product.quantity > 20:
            return "Average"
        return "low"


# if we want to see the numbers of products that have been selected for any particular collection so we can see these in this collection list with the help of annotate we can create new column for see these


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_counts']

    def products_counts(self, collection):
        return collection.products_counts

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_counts=Count('product')

        )
