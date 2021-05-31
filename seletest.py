from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\DELL\Downloads\foody-crawler\chromedriver.exe")
driver.get("https://thanhnien.vn/giai-tri/bo-vhttdl-noi-gi-ve-don-de-nghi-thu-hoi-danh-hieu-nsut-cua-hoai-linh-1390613.html")
elem = driver.find_element_by_id("btnggsearch")
elem.click()
elem = driver.find_element_by_id("txtsearch")
elem.send_keys("Hoài Linh")
elem.send_keys(Keys.ENTER)
