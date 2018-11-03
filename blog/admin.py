from django.contrib import admin

from .models import BlogPost



class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(BlogPost, BlogPostAdmin)
