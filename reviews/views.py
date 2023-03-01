from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import OnlyAdminAndCriticCanCreate
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [OnlyAdminAndCriticCanCreate]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_found = get_object_or_404(Movie, pk=self.kwargs.get("movie_id"))

        return Review.objects.filter(movie=movie_found)

    def perform_create(self, serializer):
        movie_found = get_object_or_404(Movie, pk=self.kwargs.get("movie_id"))

        serializer.save(
            critic=self.request.user,
            movie=movie_found,
        )
