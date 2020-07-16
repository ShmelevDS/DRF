from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

MAX_OBJECTS = 20


def polls_list(request):
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {'results': list(polls.values('question', 'author__username', 'created', 'updated'))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        'result': {
            'question': poll.question,
            'author': poll.author.username,
            'created': poll.created,
            'updated': poll.updated
        }
    }
    return JsonResponse(data)
