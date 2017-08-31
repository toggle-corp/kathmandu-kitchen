from django.views.generic import View
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import translation

from blog.models import Post


class BlogView(View):
    def get(self, request):
        context = {}
        posts = Post.objects.all()
        paginator = Paginator(posts, 8)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            posts = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            posts = paginator.page(page)

        language = request.GET.get('language')
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = \
                language

        current_language = translation.get_language()

        context['current_language'] = current_language
        context['next_language'] = 'en' if current_language == 'nl' \
            else 'nl'

        context['posts'] = posts

        page = int(page)
        context['current_page'] = page

        if page > 1:
            context['last_page'] = page - 1
        if page < paginator.num_pages:
            context['next_page'] = page + 1

        context['pages'] = list(range(1, paginator.num_pages+1))

        return render(request, 'blog/blog.html', context)


class PostView(View):
    def get(self, request, slug):
        context = {}
        context['post'] = Post.objects.get(slug=slug)

        language = request.GET.get('language')
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = \
                language

        current_language = translation.get_language()
        context['current_language'] = current_language
        context['next_language'] = 'en' if current_language == 'nl' \
            else 'nl'

        return render(request, 'blog/post.html', context)
