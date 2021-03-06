# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ralph.util import pricing
from ralph.discovery.models import IPAddress


def run_job(ip_address):
    try:
        ip = IPAddress.objects.select_related().get(address=ip_address)
    except IPAddress.DoesNotExist:
        return
    device = ip.device
    if not device:
        return  # no device...
    pricing.device_update_cached(device)
