from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Optionen :D
options = Options()
options.add_argument("--headless")

# Treiber
driver = webdriver.Firefox(options=options)

# URL Definition
url = "https://pastebin.ga/"

driver.get(url)
#Zum Sichergehen das er die Seite richtig durchlädt
time.sleep(2)
# Suchen von den Elementen die er braucht zum Leechen
driver.find_element_by_id("gsc-i-id1").send_keys(str(input("Enter Keyword: ")))

#driver.find_element_by_id("gsc-search-button gsc-search-button-v2").click()
driver.find_element_by_xpath("//table[@class='gsc-search-box']/tbody[1]/tr[1]/td[2]/button[1]").send_keys(Keys.ENTER)
time.sleep(5)
driver.save_screenshot("Test1.png") # Debug Code
#noch mal sicher gehen :D
time.sleep(4)
# Raus da!
driver.quit()
