from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsFreeForReading


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsFreeForReading]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
