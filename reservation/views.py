from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import translation

from mail_templated import send_mail

from reservation.models import Reservation
from branch.models import Branch


class ReservationCompleteView(View):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        context = {
            'reservation': reservation,
        }
        return render(request, 'reservation-complete.html', context)


class ReservationView(View):
    def post(self, request, branch_code):
        reservation = Reservation()
        reservation.branch = Branch.objects.get(code=branch_code)

        reservation.date = request.POST.get('date')
        reservation.time = request.POST.get('time')
        reservation.persons = int(request.POST.get('persons'))
        reservation.email = request.POST.get('email')

        reservation.save()

        language = request.POST.get('language')
        if language:
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = \
                language

        context = {
            'reservation': reservation,
            'url': request.build_absolute_uri(
                reverse('acknowledge-reservation', args=[reservation.id]))
        }

        send_mail('reservation-mail.html',
                  context,
                  'info@togglecorp.com',             # from
                  [reservation.branch.admin_email]   # to
                  )

        return redirect('reservation-complete', reservation.id)


class AcknowledgeReservataion(LoginRequiredMixin, View):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        current_language = translation.get_language()
        context = {
            'reservation': reservation,
            'current_language': current_language,
        }
        return render(request, 'acknowledge-reservation.html', context)

    def post(self, request, reservation_id):
        reservation = Reservation.objects.get(pk=reservation_id)
        reservation.status = request.POST.get('status')
        reservation.save()

        context = {
            'reservation': reservation,
        }

        send_mail('acknowledge-email.html',
                  context,
                  'info@togglecorp.com',    # from
                  [reservation.email]       # to
                  )

        return redirect('home')
