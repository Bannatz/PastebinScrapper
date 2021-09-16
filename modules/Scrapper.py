from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

class Scrapper
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

        old_results = ""
        for i in range(1,20):
            results = driver.find_element_by_xpath("(//a[@class='gs-title'])["+str(i)+"]").get_attribute("data-ctorig")
            if results != old_results:
                print(results)
                old_results = results

        driver.quit()

