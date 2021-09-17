from modules.Scrapper import *
import sys
k = input("Enter Keyword: ")

p = Scrapper.Scraping(k)

for url in p:
    u = Scrapper.TextScrape(url)
    if u is not None:
        print(u)
    else:
        print("-----ENDE-----")
sys.exit()
