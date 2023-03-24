from .serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, permissions
from userapp .models import BlogPost, Comment
from userapp.serializers import BlogPostSerializer, CommentSerializer


class BlogPostAdminList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]


class BlogPostAdminDetail(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]


class BlogPostDelete(generics.RetrieveDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]





class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        blog_post_id = self.kwargs['blog_post_id']
        try:
            blog_post = BlogPost.objects.get(id=blog_post_id)
        except BlogPost.DoesNotExist:
            return Comment.objects.none()

        return Comment.objects.filter(post=blog_post)


class CommentDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]




class AdminUserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_staff = True
        user.save()
