# from .models import Users
# from rest_framework.authtoken.models import Token

# def create_user(email, password):
#     user = Users.objects.create_user(email=email, password=password)
#     token, created = Token.objects.get_or_create(user=user)
#     user.token = token
#     user.save()
#     return user