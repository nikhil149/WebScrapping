from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = "F:\python\Devlopment\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

time.sleep(15)

details = ["Nikhil", "Rachawar", "nikhil123rachawar@gmail.com"]
count = 0
first_name = driver.find_element_by_name("fName")
first_name.send_keys(details[0])
last_name = driver.find_element_by_name("lName")
last_name.send_keys(details[1])
email_add = driver.find_element_by_name("email")
email_add.send_keys(details[2])

email_add.submit()


# driver.quit()
