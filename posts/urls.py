from django.urls import path
from .views import *

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("posts/", posts_list, name="posts"),
    path("posts/my", my_posts, name="my_posts"),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path("posts/new/", create_post, name="create_post"),
    path("posts/<int:post_id>/delete/", delete_post, name="delete_post"),
]

