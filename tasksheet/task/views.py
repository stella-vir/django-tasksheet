from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import Room, Status


def index(req):
    lastest_room_list = Room.objects.order_by('-pub_date')[:5]
    context = {'lastest_room_list': lastest_room_list}
    return render(req, 'task/index.html', context)
    # return HttpResponse("Hello, world. Task index.")
def detail(req, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(req, 'task/detail.html', {'room': room})
    # return HttpResponse('You are looking at room %s.' % room_id)
def rate(req, room_id):
    room = get_object_or_404(Room, pk=room_id)
    try:
        selected_status = room.status_set.get(pk=req.POST['status'])
    except (KeyError, Status.DoesNotExist):
        return render(req, 'task/detail.html', {'room': room, 'error_message': 'You need to make a decision.', })
    else:
        selected_status.rates += 1
        selected_status.save()
        # after post, redirect
        return HttpResponseRedirect(reverse('task:results', args=(room.id,)))
        # return HttpResponse(resp % room_id)

def results(req, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(req, 'task/results.html', {'room': room})







# end
