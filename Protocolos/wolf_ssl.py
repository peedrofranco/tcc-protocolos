import socket
import wolfssl
from functions_generics import decode_utf

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
secure_socket = wolfssl.wrap_socket(sock)
secure_socket.connect(("www.google.com.br", 443))
secure_socket.write(b"GET / HTTP/1.1\n\n")
print(decode_utf(secure_socket.read()))

secure_socket.close()

# b'HTTP/1.1 200 OK\r\nDate: Sat, 18 Apr 2020 21:10:59 GMT\r\nExpires: -1\r\n
# Cache-Control: private, max-age=0\r\nContent-Type: text/html;
# charset=ISO-8859-1\r\nP3P: CP="This is not a P3P policy!
# See g.co/p3phelp for more info."\r\nServer: gws\r\n
# X-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\n
# Set-Cookie: 1P_JAR=2020-04-18-21; expires=Mon,
# 18-May-2020 21:10:59 GMT; path=/; domain=.google.com; Secure\r\n
# Set-Cookie: NID=202=sYyMzsmEcBQ6hECLh-X_pQuR1yuN-w9rkda_XTDIaRQ2fKQ_kxXnmz86n
# iwFIMODCBAS6hiT6sBRro1wHN-DMwz1MzZU9mqQXVIwQJia4yhEvF0QHaV-CgN2R2MS7k2o4qEAMZ
# wIzGl9PgpSZPGeVmA_rcB-ghdV1AqEUV6R9-g; expires=Sun, 18-Oct-2020 21:10:59 GMT;
# path=/; domain=.google.com; HttpOnly\r\nAlt-Svc: quic=":443"; ma=2592000;
# v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,
# h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443";
# ma=2592000,h3-T050=":443"; ma=2592000\r\nAccept-Ranges: none\r\n
# Vary: Accept-Encoding\r\nTransfer-Encoding: chunked\r\n\r\n63a0\r\n
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"
# lang="pt'


# HTTP/1.1 200 OK
# Date: Mon, 20 Apr 2020 13:26:01 GMT
# Expires: -1
# Cache-Control: private, max-age=0
# Content-Type: text/html; charset=ISO-8859-1
# P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
# Server: gws
# X-XSS-Protection: 0
# X-Frame-Options: SAMEORIGIN
# Set-Cookie: 1P_JAR=2020-04-20-13; expires=Wed, 20-May-2020 13:26:01 GMT;
# path=/; domain=.google.com; Secure
# Set-Cookie: NID=202=qBxjWVSdtE7zjeC4DdRqgsKSSpqbTETSX31FD_
# -T72jYpcytPokPmqGSvdGTUeLOClQBigH5g1L8Rz5JYGBH94SXOtj_ZdDlkN5kv4lNy0aJozp351J
# 6IpdK6jrX0bWztcWOe7gXBGau1rzR-KCZyNsW0tqGx2OcXE_1-pj1LP8; expires=Tue,
# 20-Oct-2020 13:26:01 GMT; path=/; domain=.google.com; HttpOnly
# Alt-Svc: quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,
# h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443";
# ma=2592000,h3-Q043=":443"; ma=2592000,h3-T050=":443"; ma=2592000
# Accept-Ranges: none
# Vary: Accept-Encoding
# Transfer-Encoding: chunked
#
# 6562
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"
# lang="pt
