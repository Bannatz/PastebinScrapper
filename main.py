from modules.Scrapper import *
from modules.format import *
import sys, os

def get_mode(input):

    switcher = {
        "1":0,
        "2":1
        }

    s = switcher.get(m, None)
    return s


print("""\
Welcome

[1] all
[2] only email:pass

""")
m = str(input())

m = get_mode(m)
if m == None:
    m = 0

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

print(combo_list) # temp

sys.exit()
