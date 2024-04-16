from ninja import ModelSchema
from user.models import User

class UserSchema(ModelSchema):
    class Meta:
        model= User
        fields= ('id', 'email', 'name','date_of_birth','mobile_number','is_staff','is_active' )
