from modules.Scrapper import *
import sys
k = input("Enter Keyword: ")

p = Scrapper.Scraping(k)

for url in p:
    try:
        u = Scrapper.TextScrape(url)
        if ":" in u:
            print(u)
        else:
            print("Leider sind da nicht mehr drinne :(")
    except TypeError:
        print("Leider keine Combos :(")
        sys.exit()
