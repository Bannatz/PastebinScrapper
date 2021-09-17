from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

class Scrapper():
    def Scraping(keyword):
        try:
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
        except Exception:
            print("Atilla ist ein Hurensohn!")
        
        finally:
            driver.close()
            driver.quit()

    def check(string, mode):
        string = string.split("\n")
        list = []
        for blabla in string:
            if ":" in blabla or ";" in blabla:
                if "http" not in blabla and "www" not in blabla:
                    if mode == 1:
                        if "@" in blabla:
                            list.append(str(blabla))
                    else:
                        list.append(str(blabla))
        return list


    def TextScrape(url, mode):
        try:
            options = Options()
            options.add_argument("--headless")

            # Treiber für das Gute Alte Pastebin
            driver = webdriver.Firefox(options=options)

            driver.get(url)
            print(url)
            time.sleep(1)
            s = driver.find_element_by_xpath("//div[@class='page']/following-sibling::div[1]").text
            s = Scrapper.check(str(s), mode)
            return s
        except Exception:
            print("Something went wroooong :o")
        finally:
            driver.close()
