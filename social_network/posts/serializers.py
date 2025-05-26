from rest_framework import serializers
from .models import Comment, Post, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "author", "text", "created_at"]
        read_only_fields = ["author", "created_at"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post", "author"]
        read_only_fields = ["author"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "text", "image", "created_at"]
        read_only_fields = ["id", "author", "created_at"]


class PostDetailsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "text", "image", "created_at", "comments", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()
