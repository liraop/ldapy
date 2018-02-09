"""
module for LDAP component models
give a thought on naming
"""

class Domain(object):

    def __init__(self, server_url, user, pw, domainType):
        self.url = server_url
        self.bind_user = user
        self.bind_pw = pw
        self.kind = domainType

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, server_url):
        self._url = server_url

    @property
    def bind_user(self):
        """Bind user for connection"""

        return self._bind_user

    @bind_user.setter
    def bind_user(self, user):
        self._bind_user = user

    @property
    def bind_pw(self):
        """Bind user's password"""
        return self._bind_pw

    @bind_pw.setter
    def bind_pw(self, password):
        self._bind_pw = password

    @property
    def kind(self):
        """Domain's implementation kind - LDAP, AD..."""
        return self._kind

    @kind.setter
    def kind(self, impl):
        self._kind = impl
