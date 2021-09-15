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
            proxy = str(proxy).replace("\n", "")
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
