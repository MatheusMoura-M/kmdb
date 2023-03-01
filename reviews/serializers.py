from rest_framework import serializers
from .models import Review
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    critic = serializers.SerializerMethodField()

    def get_critic(self, obj):
        asd = User.objects.get(pk=obj.critic_id)
        return {
            "id": asd.id,
            "first_name": asd.first_name,
            "last_name": asd.last_name,
        }

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie",
            "critic",
        ]
        read_only_fields = ["id", "movie", "critic"]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
