# -*- coding: utf-8 -*-
import datetime
import logging

from django.conf import settings
from django.contrib import auth


class Authenticate:
    def authenticate(self, **kwargs):
        if kwargs.get('ip_authentication', False):
            return self.get_user(1)

    def get_user(self, user_id):
        try:
            return auth.models.User.objects.get(pk=user_id)
        except auth.models.User.DoesNotExist:
            return None


class Middleware:
    def process_request(self, request):
        remote_ip = request.META['REMOTE_ADDR']
        valid_ips = getattr(settings, 'VALID_IP_NUMBERS', [])
        if remote_ip in valid_ips:
            request.user = auth.authenticate(request = request, ip_authentication = True)
            logging.info("IP authentication for IP number %s", remote_ip)
        else:
            logging.error("IP authentication FAILED for IP number %s", remote_ip)
