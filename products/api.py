from ninja import NinjaAPI
from products.models import Category, Item
from products.schemas import CategorySchema, ItemSchema

app = NinjaAPI()

@app.get('categories/', response=list[CategorySchema])
def get_categories(request):
    return Category.objects.all()

@app.get('items/', response=list[ItemSchema])
def get_items(request):
    return Item.objects.all()