from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import (
    PostSerializer,
    PostDetailsSerializer,
    CommentSerializer,
    LikeSerializer,
)
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer = PostSerializer
    serializer_detailed = PostDetailsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_detailed
        return self.serializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
