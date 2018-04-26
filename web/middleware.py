from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, Template, RequestContext
from datetime import date, datetime, timedelta
from django.conf import settings
from django.contrib import auth

import getpass
import logging
import urllib
import os
import json
import requests
import commands

from smartsoccer.models import *
from datetime import date, timedelta
from django.middleware import csrf
from django.db import connection
from django.db import transaction

from app.models import Article

class DefaultMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            request.parent_category = ParentCategory.objects.filter(channel_status='1')
        except Exception:
            pass

        try:
            request.category = CategoryArticle.objects.filter(channel_status='1')
        except Exception:
            pass

    def process_request(self, request):
        pass


class PortalMiddleware(object):
    
    def process_request(self, request):
    	# print(request.path)
    	if request.path.startswith('/portal/'):

    		if not request.user.is_superuser:
				try:
					if request.user.userprofile.user_type not in ['author', 'editor']:
						return HttpResponseRedirect('/login/')
				except:
					return HttpResponseRedirect('/login/')


        if request.user.is_authenticated() and request.path == '/login/':
            return HttpResponseRedirect('/')

        if request.user.is_authenticated() and request.path == '/register/':
            return HttpResponseRedirect('/')

        if request.path.startswith('/api/article/'):
            try:
                get_slug            = request.path.split('/')[3]
                get_article         = Article.objects.get(slug = get_slug)
                get_article.view    += 1
                get_article.save()
            except:
                pass


