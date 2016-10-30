#!/bin/python

try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest

import json


class RESTfulApi:
    """
    Generic REST API call
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def request(self, url):
        """
        Web request
        :param: url: The url link
        :return JSON object
        """
        req = urlrequest.Request(url, None, headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "User-Agent": "curl/7.24.0 (x86_64-apple-darwin12.0)"})
        res = urlrequest.urlopen(req)
        res = json.loads(res.read().decode('utf8'))
        return res


