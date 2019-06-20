#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import json
import re
import requests
from urllib import quote_plus

class RestClient(object):
    @staticmethod
    def get(url, params={}):
        """
        Invoke an HTTP GET request on a url
        
        Args:
            url (string): URL endpoint to request
            params (dict): Dictionary of url parameters

        Returns:
            dict: JSON response as a dictionary

        """
        req_url = url
        
        if (len(params) > 0):
            req_url = u"{}?{}".format(url, urlencode_utf8(params))

        print(req_url)
	result = requests.get(req_url)

        if result.status_code == 200:
            return json.loads(result.text)
        else:
            raise MtgException("Failed to fetch information")


def urlencode_utf8(params):
    """
    Encode a dictionary of parameters into an '&' seperated list of url safe
    pairs seperated by '='

    Args:
        params (dict): Dictionary of url parameters

    Returns:
        utf8 string: Encoded parameter string
    """
    param_strings = []
    for key, value in params.items():
        if not isinstance(key, unicode):
            key_str = str(key)
        else:
            key_str = quote_plus(key.encode('utf8'))
        if not isinstance(value, unicode):
            val_str = str(value)
        else:
            val_str = quote_plus(value.encode('utf8'))

        param_strings.append(u"{}={}".format(key_str, val_str))

    return u'&'.join(param_strings)


class MtgException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description
