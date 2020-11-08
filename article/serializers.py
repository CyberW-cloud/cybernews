from rest_framework import serializers

from .models import Article, Comment, Vote


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ("id", "author_name", "creation_date", "content")

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author_name = instance.author_name
        instance.content = validated_data.get("content", instance.content)
        instance.creation_date = instance.creation_date
        instance.article = instance.article
        instance.save()
        return instance


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField()
    amount_of_comments = serializers.SerializerMethodField()
    amount_of_upvotes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    @staticmethod
    def get_amount_of_comments(obj):
        return Comment.objects.filter(article=obj).count()

    @staticmethod
    def get_amount_of_upvotes(obj):
        return Vote.objects.filter(article=obj).count()

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.link = validated_data.get("link", instance.link)
        instance.creation_date = instance.creation_date
        instance.author_name = instance.author_name
        instance.save()
        return instance
