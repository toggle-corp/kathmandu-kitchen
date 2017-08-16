from django.views.generic import View
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Post


class BlogView(View):
    def get(self, request):
        context = {}
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            posts = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            posts = paginator.page(page)

        context['posts'] = posts

        page = int(page)
        context['page'] = page

        if page > 1:
            context['last_page'] = page - 1
        if page < paginator.num_pages:
            context['next_page'] = page + 1

        return render(request, 'blog/blog.html', context)


class PostView(View):
    def get(self, request, slug):
        context = {}
        return render(request, 'blog/post.html', context)
