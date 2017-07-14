from django.conf.urls import url, static
from django.contrib import admin
from django.conf import settings

from .views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view()),
    url(r'^(?P<code>\w+)/$', HomeView.as_view(), name='home'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
