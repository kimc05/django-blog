from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get(self, request):
        published = Post.objects.exclude(published_date__exact=None)
        posts = published.order_by('-published_date')
        context = {'post_list': posts}
        return render(request, 'blogging/list.html', context)



class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def detail_view(self, request, post_id):
        published = Post.objects.exclude(published_date__exact=None)
        try:
            post = published.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        context = {'post': post}
        return render(request, 'blogging/detail.html', context)
