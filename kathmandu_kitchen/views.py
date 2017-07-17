from django.views.generic import View
from django.shortcuts import render, redirect
from django.utils import translation

from branch.models import Branch
from menu.models import MenuCategory


class HomeView(View):
    def get(self, request, code=None):
        if Branch.objects.count() > 0:
            if not code:
                return redirect('home', Branch.objects.all()[0].code)
        context = {}

        context['branches'] = Branch.objects.all()
        context['categories'] = MenuCategory.objects.filter(branch__code=code)
        context['current_branch'] = Branch.objects.get(code=code)

        language = request.GET.get('language')
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = \
                language

        current_language = translation.get_language()

        context['current_language'] = current_language
        context['next_language'] = 'en' if current_language == 'nl' \
            else 'nl'

        return render(request, 'home.html', context)
