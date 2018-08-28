#!/usr/bin/env python3
import json
import logging
import requests
import re

class ComcastData:

  def __init__(self, username, password, debug = False, ):
    self.logger = logging.getLogger(__name__)
    self.logger.propagate = debug
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('requests').setLevel(logging.ERROR)
    self.session = requests.Session()
    self.username = username
    self.password = password


  def get(self):

    self.logger.debug("Finding req_id for login...")
    res = self.session.get('https://customer.xfinity.com/oauth/force_connect/?continue=%23%2Fdevices')
    assert res.status_code == 200

    m = re.search(r'<input type="hidden" name="reqId" value="(.*?)">', res.text)
    req_id = m.group(1)
    self.logger.debug("Found req_id = %r", req_id)

    data = {
      'user': self.username,
      'passwd': self.password,
      'reqId': req_id,
      'deviceAuthn': 'false',
      's': 'oauth',
      'forceAuthn': '1',
      'r': 'comcast.net',
      'ipAddrAuthn': 'false',
      'continue': 'https://oauth.xfinity.com/oauth/authorize?client_id=my-account-web&prompt=login&redirect_uri=https%3A%2F%2Fcustomer.xfinity.com%2Foauth%2Fcallback&response_type=code&state=%23%2Fdevices&response=1',
      'passive': 'false',
      'client_id': 'my-account-web',
      'lang': 'en',
    }

    self.logger.debug("Posting to login...")
    res = self.session.post('https://login.xfinity.com/login', data=data)
    assert res.status_code == 200

    self.logger.debug("Fetching internet usage AJAX...")
    res = self.session.get('https://customer.xfinity.com/apis/services/internet/usage')
    self.logger.debug("Resp: %r", res.text)
    assert res.status_code == 200

    return json.loads(res.text)
