import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "169.254.108.225", 8888)
socket.socket = socks.socksocket
import urllib2
print urllib2.urlopen('http://www.google.co.jp/').read()

