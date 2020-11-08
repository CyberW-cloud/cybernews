from django.urls import path

from .views import ArticleView, CommentView, UpvoteView

app_name = "articles"

urlpatterns = [
    path("articles/", ArticleView.as_view()),
    path("articles/<int:pk>", ArticleView.as_view()),
    path("articles/<int:article_id>/comments", CommentView.as_view()),
    path("articles/<int:article_id>/comments/<int:pk>", CommentView.as_view()),
    path("articles/<int:article_id>/vote", UpvoteView.as_view()),
]
