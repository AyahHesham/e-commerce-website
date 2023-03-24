from django.contrib.auth.backends import ModelBackend,UserModel
from django.contrib.auth.models import User
from django.db.models import Q


#we will use 2 available function and make override on them
class emailBackend(ModelBackend):
    #
    def authenticate(self, request,username=None, password=None, **kwargs):
        # for if user recorded or not
        try:
            user=User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            pass
        except Multibleobjectreturned:
            return User.objects.filter(email=username).order_by(id).first()
        else:
            if user.check_password(password)and self.user_can_authenticate(user):
                return user
        