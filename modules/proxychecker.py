from ProxyScraper import *
import urllib.request, socket, urllib.error,threading

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

def Check(s):
    for proxy in s:
        if is_bad_proxy(proxy):
            print("Bad Proxy: " + proxy)
        else:
            print("Good Proxy: " + proxy)



