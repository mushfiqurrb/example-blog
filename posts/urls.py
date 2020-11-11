from django.urls import path
from posts.views import posts, post_details,post_comments

urlpatterns = [
    path('', posts),
    path('<int:post_id>', post_details),
    path('<int:post_id>/comments', post_comments),
]
