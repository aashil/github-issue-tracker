from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://github.com/scikit-learn/scikit-learn/issues")

elem = driver.find_element_by_id("js-issues-search")
elem.clear()
elem.send_keys("is:open is:issue label:Easy")
elem.send_keys(Keys.RETURN)
driver.close()

