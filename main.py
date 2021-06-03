from selenium import webdriver

driver_path = "F:\python\Devlopment\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_saleprice")
# # print(price.text)
# time = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
#
# event = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')

my_dict = {}

for i in range(1, 6):
    time = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    event = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    print(time.text)
    print(event.text)
    my_dict[i-1] = {
        'time': time.text,
        'event': event.text
    }

print(my_dict)
driver.quit()