from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

class Scrapper():
    def Scraping(keyword):
        global driver
        options = Options()
        options.add_argument("--headless")

        # Treiber
        driver = webdriver.Firefox(options=options)

        # URL Definition
        url = "https://pastebin.ga/"

        driver.get(url)

        # Suchen von den Elementen die er braucht zum Leechen
        driver.find_element_by_id("gsc-i-id1").send_keys(str(keyword))

        driver.find_element_by_xpath("//table[@class='gsc-search-box']/tbody[1]/tr[1]/td[2]/button[1]").send_keys(Keys.ENTER)

        time.sleep(3)

        # Attila Du Hurensohn
        # Remove the Log File because its like Attila!
        rm_file = ["geckodriver.log"]
    
        for file in rm_file:
            os.remove(file)

        r_results = []
        old_results = ""
        for i in range(1,20):
            results = driver.find_element_by_xpath("(//a[@class='gs-title'])["+str(i)+"]").get_attribute("data-ctorig")
            if results != old_results:
                r_results.append(results)
                old_results = results
        return r_results

        driver.quit()

