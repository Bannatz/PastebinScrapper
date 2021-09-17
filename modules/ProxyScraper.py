import sys
import os
import urllib, urllib.request

class scrape():

    def http(timeout): # min timout is 50 | max timout is 1000
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_http")

        clean_proxys = []

        f = open("proxys_http", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxy).replace("\n", "")
            
            c = check.check("http", proxy, timeout)
            if c == 1:
                print(proxy+" Working")
                clean_proxys.append(proxy)
            else:
                print(proxy+" Failed")

        f.close()

        return clean_proxys


    def socks4(timeout):
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_socks4")
        
        clean_proxys = []

        f = open("proxys_socks4", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxy).replace("\n", "")

            c = check.check("socks4", proxy, timeout)
            if c == 1:
                print(proxy+" Working")
                clean_proxys.append(proxy)
            else:
                print(proxy+" Failed")

            clean_proxys.append(proxy)

        f.close()
        
        return clean_proxys


    def socks5(timeout):
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_socks5")

        clean_proxys = []

        f = open("proxys_socks5", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxy).replace("\n", "")

            c = check.check("socks5", proxy, timeout)
            if c == 1:
                print(proxy+" Working")
                clean_proxys.append(proxy)
            else:
                print(proxy+" Failed")

            clean_proxys.append(proxy)

        f.close()

        return clean_proxys

class check():

    def check(type, proxy, timeout):
        t = timeout
        try:
            p = urllib.request.ProxyHandler({str(type):str(proxy)})
            o = urllib.request.build_opener(p)
            o.addheaders = [("User-agent", "Mozilla/5.0")]
            urllib.install_opener(o)
            req = urllib.Request("http://www.google.de")
            sock = urllib.urlopen(req)
            r = 1
        except Exception:
            r = 2

        return r
