from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from html.parser import HTMLParser as parser
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import time
import os

def Scraping():
    global driver
    # Optionen :D
    options = Options()
    options.add_argument("--headless")

    # Treiber
    driver = webdriver.Firefox(options=options)

    #https://pastebin.ga/

    # URL Definition
    url = "https://pastebin.ga/"

    driver.get(url)

    # Suchen von den Elementen die er braucht zum Leechen
    driver.find_element_by_id("gsc-i-id1").send_keys(str(input("Enter Keyword: ")))

    driver.find_element_by_xpath("//table[@class='gsc-search-box']/tbody[1]/tr[1]/td[2]/button[1]").send_keys(Keys.ENTER)

    time.sleep(3)

    driver.save_screenshot("Test1.png") # Debug Code

    # Attila Du Hurensohn
    #driver.quit()
    # Remove the Log File because its like Attila!
    rm_file = ["geckodriver.log"]
    
    for file in rm_file:
        os.remove(file)
    
    results  = driver.find_element_by_xpath("(//a[@class='gs-title'])[1]").get_attribute("data-ctorig")
    print(results) 

Scraping()
driver.quit()

