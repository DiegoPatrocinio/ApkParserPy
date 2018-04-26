# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, Template, RequestContext
from django.template import Template as template_django
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.conf import settings
from django import forms

from backoffice.models import *

import re
import uuid

import logging

log = logging.getLogger("backoffice")
log.setLevel(logging.DEBUG)


def home(request):
    return HttpResponseRedirect('/admin')
