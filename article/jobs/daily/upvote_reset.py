from django_extensions.management.jobs import DailyJob

from article.models import Vote


class Job(DailyJob):
    """
    Daily job to reset post upvotes count
    """

    def execute(self):
        Vote.objects.all().delete()
