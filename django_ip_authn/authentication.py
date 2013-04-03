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
        header = getattr(settings, 'REMOTE_IP_HEADER', 'REMOTE_ADDR')
        remote_ip = request.META.get(header, None)
        valid_ips = getattr(settings, 'VALID_IP_NUMBERS', [])
        if remote_ip and remote_ip in valid_ips:
            user = auth.authenticate(request = request, ip_authentication = True)
            if user:
                request.user = user
                logging.info("IP authentication for IP number %s", remote_ip)
            else:
                logging.info("IP authenticatoin for IP number %s worked, but a user was not found",
                    remote_ip)
        else:
            logging.warning(
                "IP authentication FAILED for IP number %s (headers are %s)",
                remote_ip, request.META.keys())
