from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

#custom authentication class to authenticate using email
class Emailbackend(ModelBackend):
    def authenticate(self, request,  username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
