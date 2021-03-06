from django.conf.urls import url, static, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login

from .views import HomeView
from reservation.views import ReservationView, \
    ReservationCompleteView, AcknowledgeReservataion
from blog.views import BlogView, PostView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', login,
        kwargs={"template_name": "admin/login.html"}),

    url(r'^reservation-complete/(?P<reservation_id>\d+)/$',
        ReservationCompleteView.as_view(),
        name='reservation-complete'),

    url(r'^reserve/(?P<branch_code>\w+)/$', ReservationView.as_view(),
        name='reserve'),

    url(r'^acknowledge-reservation/(?P<reservation_id>\d+)/$',
        AcknowledgeReservataion.as_view(),
        name='acknowledge-reservation'),

    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', PostView.as_view(), name='blog_post'),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^(?P<code>\w+)/$', HomeView.as_view(), name='home'),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
