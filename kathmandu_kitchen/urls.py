from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', admin.site.urls),
]
