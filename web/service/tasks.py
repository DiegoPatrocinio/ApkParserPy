#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import re

from celery import task

from restclient import GET, POST, PUT, DELETE
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage
import json
import time


@task()
def email_send(subject, to, msg, fr=None, title=''):
    print 'subject: %s' % subject
    print 'to: %s' % to
    headers = {'Reply-To': fr}

    while True:
        try:
            subject = subject
            html_content = msg
            to = [to]
            e = EmailMessage(subject, html_content, '%s <%s>' % (title, fr), to, headers=headers)
#            if attachment_id:
#                for i in json.loads(attachment_id):
#                    f = Attachment.objects.get(id=i)
#                    e.attach(f.file.name, f.file.read())
            e.content_subtype = "html"
            e.send(fail_silently=False)
        except Exception, err:
            print err
            break
        else:
            print 'Email Status: Success to: %s' % to
            break
    return True
