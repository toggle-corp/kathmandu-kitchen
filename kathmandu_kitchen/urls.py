from django.conf.urls import url, static
from django.contrib import admin
from django.conf import settings

from .views import HomeView
from reservation.views import ReservationView, \
    ReservationCompleteView, AcknowledgeReservataion


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),

    url(r'^reservation-complete/(?P<reservation_id>\d+)/$',
        ReservationCompleteView.as_view(),
        name='reservation-complete'),

    url(r'^reserve/(?P<branch_code>\w+)/$', ReservationView.as_view(),
        name='reserve'),

    url(r'^acknowledge-reservation/(?P<reservation_id>\d+)/$',
        AcknowledgeReservataion.as_view(),
        name='acknowledge-reservation'),

    url(r'^(?P<code>\w+)/$', HomeView.as_view(), name='home'),

] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
