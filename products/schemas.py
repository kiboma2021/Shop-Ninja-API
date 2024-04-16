from ninja import ModelSchema
from products.models import Category, Item

class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        fields = ('id','date_created','name')

class ItemSchema(ModelSchema):
    category: CategorySchema | None = None

    class Meta:
        model = Item
        fields = ('id','date_created','name', 'category', 'description','slug')
