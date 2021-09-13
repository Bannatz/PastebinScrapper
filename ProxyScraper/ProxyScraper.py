import sys
import os
import urllib.request

class scrape():

    def http(timeout): # min timout is 50 | max timout is 1000
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_http")

        clean_proxys = []

        f = open("proxys_http", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxys_socks4).replace("\n", "")
            clean_proxys.append(proxy)

        f.close()

        return clean_proxys


    def socks4(timeout):
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_socks4")
        
        clean_proxys = []

        f = open("proxys", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxy).replace("\n", "")
            clean_proxys.append(proxy)

        f.close()
        
        return clean_proxys


    def socks5(timeout):
        urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout="+str(timeout)+"&country=all&ssl=all&anonymity=all&simplified=true", filename="proxys_socks5")

        clean_proxys = []

        f = open("proxys", "r")
        proxys = f.readlines()

        for proxy in proxys:
            proxy = str(proxy).replace("\n", "")
            clean_proxys.append(proxy)

        f.close()

        return clean_proxys

print("""\
ProxyScraper

[1] http
[2] Socks4
[3] Socks5
""")

s = str(input())

if s == "1":
    print("Scraping http with max timeout 3000ms")
    scrape.http(3000)
    print("finished")
    sys.exit()

elif s == "2":
    print("Scraping Socks4 with max timeout 3000ms")
    scrape.socks4(3000)
    print("finished")
    sys.exit()

elif s == "3":
    print("Scraping Socks5 with max timeout 3000ms")
    scrape.socks5(3000)
    print("finished")
    sys.exit()
