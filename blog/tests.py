from django.test import TestCase

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import BlogPost


class BlogPostModelTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = BlogPost(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = BlogPost(pub_date=time)
        self.assertIs(old_post.was_published_recently(), False)


    def test_was_published_recently_with_recent_post(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = BlogPost(pub_date=time)
        self.assertIs(recent_post.was_published_recently(), True)
