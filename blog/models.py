from django.db import models
import datetime
from django.utils import timezone

class BlogPost(models.Model):
    post_title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    content_text = models.TextField()
    upvotes = models.IntegerField(default=0)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.post_title
