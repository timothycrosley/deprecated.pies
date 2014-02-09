from __future__ import absolute_import

from ..version_info import PY3

if PY3:
    from urllib.request import *
else:
    from urllib import FancyURLopener, getproxies, pathname2url, url2pathname, urlcleanup, URLopener, urlretrieve
    from urllib2 import (AbstractBasicAuthHandler, AbstractDigestAuthHandler, BaseHandler, build_opener,
                         CacheFTPHandler, FileHandler, FTPHandler, HTTPBasicAuthHandler, HTTPCookieProcessor,
                         HTTPDefaultErrorHandler, HTTPDigestAuthHandler, HTTPHandler, HTTPPasswordMgr,
                         HTTPPasswordMgrWithDefaultRealm, HTTPRedirectHandler, HTTPSHandler, install_opener,
                         OpenerDirector, ProxyBasicAuthHandler, ProxyDigestAuthHandler, ProxyHandler, Request,
                         UnknownHandler, urlopen)
