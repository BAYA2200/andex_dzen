from django.db.models import Avg
from rest_framework import serializers
from .models import Post, Comment, Rating


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'text', 'created']

    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, ob):
        return ob.reviews.all().aggregate(Avg('rating'))['rating__avg']


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['score', 'rating']


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
