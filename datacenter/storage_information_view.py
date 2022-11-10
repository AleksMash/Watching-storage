from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
import datetime
from .models import format_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits_serialized = []
    for visit in non_closed_visits:
        duration = format_duration(visit.get_duration())
        non_closed_visits_serialized.append({
          'who_entered': visit.passcard.owner_name,
          'entered_at': localtime(visit.entered_at),
          'duration': duration,
                                 })

    context = {
        'non_closed_visits': non_closed_visits_serialized,
        'current_datetime': localtime(datetime.datetime.now
                                      (datetime.timezone.utc))
        }
    return render(request, 'storage_information.html', context)
