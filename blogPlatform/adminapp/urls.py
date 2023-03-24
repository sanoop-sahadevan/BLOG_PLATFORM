from django.urls import path
from .views import BlogPostAdminList, BlogPostAdminDetail,BlogPostDelete,CommentList,CommentDeleteView,AdminUserCreate

urlpatterns = [
    # ...
    path('admin/blog-posts/', BlogPostAdminList.as_view(), name='blog-post-admin-list'),
    path('admin/blog-posts/<int:pk>/', BlogPostAdminDetail.as_view(), name='blog-post-admin-detail'),
    path('blog_posts/<int:pk>/delete/', BlogPostDelete.as_view(), name='blog_post_delete'),
    # path('comments/<int:id>/',BlogPostCommentsList.as_view(), name='comment-detail'),
    #  path('blog-posts/comments/<int:id>', BlogPostCommentsView.as_view(), name='blog-post-comments'),
     path('blog-posts/<int:blog_post_id>/comments/', CommentList.as_view(), name='comment-list'),
      path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
      path('admin-users/create/', AdminUserCreate.as_view(), name='admin-user-create'),
    # ...
]
