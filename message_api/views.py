from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.template import loader, Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from message_api.models import Message

def index(request):
    return render_to_response(
            'message_api/index.html',
            RequestContext(request,{}))


def coke_list(request):
    Message.populate_from_api()
    allmessages = Message.objects.all().order_by('-sentiment')
    return render_to_response(
            'message_api/coke_list.html',
            RequestContext(request,
               {
                   'allmessages':allmessages
               }
            ))

def user_details(request):
    user_handle = request.GET.get('user_handle')
    if not user_handle:
        return HttpResponseRedirect('/')
    user_posts = Message.objects.filter(user_handle = '@%s' % user_handle)
    return render_to_response(
            'message_api/user_details.html',
            RequestContext(request,
               {
                   'user_posts':user_posts
               }
            ))


