from ProxyScraper import *


import urllib.request, socket, urllib.error,threading
from multiprocessing import Process, Queue

i = input("Bitte Timeout danke: ")
print("socks4, socks5, http")
t = str(input("Bitte Type eingeben: "))
th = int(input("Wie viele Threads ?: "))
if t == "socks4":
    s = scrape.socks4(t)
    
if t == "socks5":
    s = scrape.socks5(t)
    
if t == "http":
    s = scrape.http(t)


def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.example.com')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main():
    for proxy in s:
        if is_bad_proxy(proxy):
            print("Bad Proxy: " + proxy)
        else:
            print("Good Proxy: " + proxy)



processes = [Process(target=main, args=()) for x in range(th)]

for p in processes:
    p.start()

for p in processes:
    p.join()
