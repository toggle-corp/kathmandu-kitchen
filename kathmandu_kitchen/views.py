from django.views.generic import View
from django.shortcuts import render, redirect

from branch.models import Branch
from menu.models import MenuCategory


class HomeView(View):
    def get(self, request, code=None):
        if Branch.objects.count() > 0:
            if not code:
                return redirect('home', Branch.objects.all()[0].code)
        context = {}

        context['branches'] = Branch.objects.all()
        context['categories'] = MenuCategory.objects.all()
        context['current_branch'] = Branch.objects.get(code=code)

        return render(request, 'home.html', context)