from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreSerializer
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

    def create(self, validated_data: dict) -> Movie:
        genres_list = validated_data.pop("genres")
        movie_obj = Movie.objects.create(**validated_data)

        for genre_dict in genres_list:
            genreFound = Genre.objects.filter(name__iexact=genre_dict["name"]).first()

            if not genreFound:
                genreFound = Genre.objects.create(**genre_dict)

            movie_obj.genres.add(genreFound)

        return movie_obj
