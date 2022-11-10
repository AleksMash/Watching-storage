from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    this_passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=this_passcard)
    visits_serialized = []
    for visit in visits:
        visits_serialized.append({
          'entered_at': localtime(visit.entered_at),
          'duration': format_duration(visit.get_duration()),
          'is_strange': visit.is_visit_long()
        })
    context = {
        'passcard': this_passcard,
        'this_passcard_visits': visits_serialized
    }
    return render(request, 'passcard_info.html', context)
