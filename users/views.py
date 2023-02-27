from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PermissionCuston


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionCuston]

    queryset = User.objects.all()
    serializer_class = UserSerializer
