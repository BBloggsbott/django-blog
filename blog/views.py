from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
from django.template import loader
from django.http import Http404
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BlogPost.objects.order_by('-pub_date')[:5]

def view_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/view_post.html', {'blog_post': post})

def upvote(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.upvotes += 1
    post.save()
    return view_post(request, post_id)
