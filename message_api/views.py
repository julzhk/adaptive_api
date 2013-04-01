from django import http, template
from django.conf import settings
from django import http, template
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse('booya')

