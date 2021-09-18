from ProxyScraper import *
import urllib.request, socket, urllib.error,threading
from multiprocessing import Process, Queue
def hallo():
    i = input("Bitte Timeout danke: ")
    print("http")
    th = int(input("Wie viele Threads ?: "))
  
    s = scrape.http(t)
    return s

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({"http": pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('http://www.google.com')
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False

def main(s):
    for proxy in s:
        if is_bad_proxy(t, proxy):
            print("Bad Proxy: " + proxy)
        else:
            print("Good Proxy: " + proxy)

def multikulti(s):
    processes = [Process(target=main, args=(s)) for x in range(th)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    
s = hallo()
multikulti(s)
