from django.contrib.auth.models import User


class EmailAuth:
    def authenticate(self,request,username=None,password =None):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return User
            return None 
        except(User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
    def get_user(request,user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None