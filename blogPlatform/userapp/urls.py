from django.urls import path
from .views import BlogPostList, BlogPostDetail,  BlogPostCreate, CommentCreate, CommentList, CommentDetail, RegisterAPIView

urlpatterns = [
    path('posts/', BlogPostList.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', BlogPostDetail.as_view(), name='blogpost-detail'),
    path('blog/create/', BlogPostCreate.as_view(), name='blogpost-create'),
    path('blog/comments/create/<int:post_id>',
         CommentCreate.as_view(), name='comment-create'),
    path('blog/comments/<int:post_id>/',
         CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),

    path('register/', RegisterAPIView.as_view(), name='register'),
]
