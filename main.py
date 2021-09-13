from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Optionen :D
options = Options()
options.add_argument("--headless")

# Treiber
driver = webdriver.Firefox(options=options)

# URL Definition
url = "https://pastebin.ga/"

driver.get(url)

# Suchen von den Elementen die er braucht zum Leechen
driver.find_element_by_id("gsc-i-id1").send_keys(str(input("Enter Keyword: ")))

driver.find_element_by_xpath("//table[@class='gsc-search-box']/tbody[1]/tr[1]/td[2]/button[1]").send_keys(Keys.ENTER)

time.sleep(5)
print(driver.current_url) # Eben so Debug Code!
current_url = driver.current_url

url_id = "gsc-webResult gsc-result"

urlsoup = BeautifulSoup(current_url, "html_parser")

pastebin_data = urlsoup.find_all("div", attrs={"class": url_id})

time.sleep(3)

driver.save_screenshot("Test1.png") # Debug Code

# Raus da!
driver.quit()
