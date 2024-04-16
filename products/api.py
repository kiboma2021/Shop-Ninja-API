from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from products.models import Category, Item
from products.schemas import CategorySchema, ItemSchema

app = NinjaAPI()

@app.get('categories/', response=list[CategorySchema])
def get_categories(request):
    return Category.objects.all()

@app.get('items/', response=list[ItemSchema])
def get_items(request):
    return Item.objects.all()

@app.get('items/{slug}/', response=ItemSchema)
def get_item(request, slug:str):
    item = get_object_or_404(Item,slug=slug)
    return item