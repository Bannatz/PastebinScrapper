from modules.Scrapper import *
from modules.format import *
from modules.ProxyScraper import *
from modules.proxychecker import *
from modules.checker import *
import sys, os

def get_mode(input):

    switcher = {
        "1":0,
        "2":1
        }

    s = switcher.get(m, None)
    return s


print("""\
Lets config ur session :)

what do u want to scrape?

[1] all (only good if u want user:pass)
[2] only email:pass

""")
m = str(input())
m = get_mode(m)

if m == None:
    m = 0
print("\nNow its scraping time :D\n")
k = input("\nEnter Keywords: ")

p = Scrapper.Scraping(k)

list = []

for url in p:
    u = Scrapper.TextScrape(url, m)
    if u is not None:
        list.extend(u)
    else:
        print("No combos found here :c")

combo_list = []
for c in list:
    c = c.replace(";", ":")
    c = format.combo(c)
    combo_list.append(c)

print("\nJetzt brauchen wir Proxys!")
t = input("Timeout: ")
p = scrape.http(t)
proxy_list = Check(p)
print("Finshed Proxy checking!\nNow its Account checking Time :D\n")

Checker(combo_list, proxy_list)

sys.exit()
