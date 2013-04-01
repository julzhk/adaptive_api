from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.template import loader, Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

def index(request):
        return render_to_response(
                'message_api/index.html',
                RequestContext(request,
                               {
                               }
                ))


