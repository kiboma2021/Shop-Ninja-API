from ninja import NinjaAPI
from user.models import User
from user.schemas import UserSchema

userApp = NinjaAPI()

@userApp.get('users/', response=list[UserSchema])
def get_users(request):
    return User.objects.all()