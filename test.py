from modules.Scrapper import *
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

end_list = []

for url in p:
    u = Scrapper.TextScrape(url, m)
    if u is not None:
        end_list.extend(u)
    else:
        print("No combos found here :c")
print(end_list)
combos = "\n".join(end_list)
open("combos.txt", "w").write(combos)
print("Finished")

sys.exit()
