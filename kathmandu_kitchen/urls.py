from django.conf.urls import url, static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', admin.site.urls),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
