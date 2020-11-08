from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .models import Article, Comment, Vote
from .serializers import ArticleSerializer, CommentSerializer


class ArticleView(APIView):
    @staticmethod
    def get(request, pk=None):
        if pk:
            articles = get_object_or_404(Article.objects.all(), pk=pk)
            many = False
        else:
            articles = Article.objects.all()
            many = True
        serializer = ArticleSerializer(articles, many=many)

        return Response({"articles": serializer.data})

    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            serializer = ArticleSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save(author_name=request.user)

            return Response(status=201)
        return Response(status=403)

    @staticmethod
    def put(request, pk):
        if request.user.is_authenticated:
            saved_article = get_object_or_404(
                Article.objects.all(),
                pk=pk,
            )
            serializer = ArticleSerializer(
                instance=saved_article,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            return Response(status=201)
        return Response(status=403)

    @staticmethod
    def delete(request, pk):
        if request.user.is_authenticated:

            article = get_object_or_404(Article.objects.all(), pk=pk)
            article.delete()

            return Response(status=204)
        return Response(status=403)


class CommentView(APIView):
    @staticmethod
    def get(request, article_id, pk=None):
        article = get_object_or_404(Article.objects.all(), pk=article_id)

        if pk:
            comments = get_object_or_404(Comment.objects.all(), pk=pk)
            many = False
        else:
            comments = Comment.objects.filter(article=article)
            many = True

        serializer = CommentSerializer(comments, many=many)

        return Response({"article_id": article_id, "comments": serializer.data})

    @staticmethod
    def post(request, article_id):
        if request.user.is_authenticated:

            article = get_object_or_404(Article.objects.all(), pk=article_id)
            serializer = CommentSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    author_name=request.user,
                    article=article,
                )

            return Response(status=201)
        return Response(status=401)

    @staticmethod
    def put(request, article_id, pk):
        if request.user.is_authenticated:
            saved_comment = get_object_or_404(
                Comment.objects.all(),
                pk=pk,
            )
            serializer = CommentSerializer(
                instance=saved_comment,
                data=request.data,
                partial=True,
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

            return Response(status=201)
        return Response(status=403)

    @staticmethod
    def delete(request, article_id, pk):
        if request.user.is_authenticated:

            article = get_object_or_404(Article.objects.all(), pk=article_id)
            comment = Comment.objects.filter(article=article, pk=pk)
            comment.delete()

            return Response(status=204)
        return Response(status=403)


# Vote endpoint
class UpvoteView(APIView):
    @staticmethod
    def post(request, article_id):
        if request.user.is_authenticated:
            vote = Vote.objects.filter(
                article__id=article_id, author_name__id=request.user.id
            )
            if not vote:
                # I didn't find out shorter version of creating vote obj.
                # Option like 3 rows above didn't work...
                article = Article.objects.get(id=article_id)
                user = User.objects.get(id=request.user.id)
                Vote.objects.create(article=article, author_name=user)
            return Response(status=201)
        return Response(status=401)

    @staticmethod
    def delete(request, article_id):
        if request.user.is_authenticated:

            vote = get_object_or_404(
                Vote.objects.filter(),
                article__id=article_id,
                author_name__id=request.user.id,
            )
            vote.delete()

            return Response(status=204)
        return Response(status=401)
