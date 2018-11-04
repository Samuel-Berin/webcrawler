#!/usr/bin/python

import argparse
import sys
import xml
import socket
import json
import datetime

parser = argparse.ArgumentParser(description='Crawls Fakebook for secret flags.')
parser.add_argument(type=str, dest="username", help='The username.')
parser.add_argument(type=str, dest="password", help='The password.')

args = parser.parse_args(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

fakebook_IP = socket.gethostbyname(socket.gethostname())
host = socket.gethostbyname("fring.ccs.neu.edu")
dest = (fakebook_IP, 80)
sock.connect((host, 80))
sock.settimeout(10)

sock.send("GET /accounts/login/?next=/fakebook/ HTTP/1.1\r\n")
sock.send("Connection: keep-alive\r\n")
sock.send("From: weinstein.br@husky.neu.edu\r\n")
sock.send("User-Agent: Mozilla/5.0\r\n")
sock.send("Host: fring.ccs.neu.edu\r\n")
GA = "_ga=GA1.2.1499035527." + datetime.datetime.now().strftime("%H%M%S%f")
GID = "_gid=1.2.6669032327." + datetime.datetime.now().strftime("%H%M%S%f")
sock.send("Cookie: " + GA + ";" + GID + "\r\n")
sock.send("\r\n")

result = sock.recv(1400)
result += sock.recv(1400)


print(result)

result = result[result.index("Set-Cookie") + 12:]
csrf_Cookie = result[:result.index(";")]
csrf_Cookie = csrf_Cookie[10:]   #Gets rid of csrf tag
#csrf_Cookie = "csrfmiddlewaretoken=" + csrf_Cookie


result = result[result.index("Set-Cookie") + 12:]
session_Cookie = result[:result.index(";")]


sock.send("POST /accounts/login/ HTTP/1.1 \r\n")
sock.send("Host: fring.ccs.neu.edu\r\n")
sock.send("User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0\r\n")
sock.send("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n")
sock.send("Accept-Language: en-US,en;q=0.5\r\n")
sock.send("Accept-Encoding: gzip, deflate\r\n")
sock.send("Referer: http://fring.ccs.neu.edu/accounts/login/?next=/fakebook/\r\n")
sock.send("Content-Type: application/x-www-form-urlencoded\r\n")
sock.send("Content-Length: 109\r\n")
sock.send("Cookie: " + " csrftoken=" + csrf_Cookie + "; " + session_Cookie + "\r\n")
sock.send("Connection: keep-alive\r\n")
sock.send("Upgrade-Insecure-Requests: 1\r\n")
sock.send("\r\n")
sock.send("username=001271126&password=2HEC8XA2&" + "csrfmiddlewaretoken=" + csrf_Cookie + "&next=%2Ffakebook%2F\r\n")
sock.send("\r\n")

result2 = sock.recv(1400)
#result2 += sock.recv(1400)

print("POST RESPONSE: \n")
print(result2)
print(csrf_Cookie)

#print("Cookie: " + "csrftoken=" + csrf_Cookie + ";" + session_Cookie + "\r\n")
#print("Cookie: " + "csrftoken=" + csrf_Cookie + "; " + session_Cookie + "\r\n")
#print("username=001271126&password=2HEC8XA2&" + "csrfmiddlewaretoken=" + csrf_Cookie + "&next=/fakebook/\r\n")

'''
one = str(result2[:result2.index("\'")])
result2 = result2[result2.index("=")+2:]
cook = one + "=" + str(result2[:result2.index("\'")])

'''