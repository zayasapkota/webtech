from rest_framework import serializers
from .models import CommentNRating


class CommentNRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentNRating
        fields = ('__all__')
