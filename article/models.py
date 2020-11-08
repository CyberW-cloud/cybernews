from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(
        name="title",
        max_length=120,
        null=False,
    )
    link = models.URLField(
        name="link",
        unique=True,
        null=False,
    )
    creation_date = models.DateField(
        name="creation_date",
        default=date.today,
        null=False,
    )
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        null=False,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_name",
    )
    content = models.CharField(
        name="content",
        max_length=300,
        blank=False,
        null=False,
    )
    creation_date = models.DateField(
        name="creation_date",
        default=date.today,
        null=False,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self):
        return f"{self.author_name.username} - {self.article.title}"


class Vote(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "vote"
        constraints = [
            models.UniqueConstraint(
                fields=["article", "author_name"], name="unique_article_votes"
            ),
        ]

    def __str__(self):
        return f"{self.author_name.username} - {self.article.title}"
