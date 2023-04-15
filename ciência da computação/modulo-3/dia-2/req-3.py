from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox()

firefox.get("https://diolinux.com.br/")

nex_button = True
counter = 0

while (nex_button and counter < 10):
    nex_button = firefox.find_element("class name", "btn-load-more")
    nex_button.click()
    counter += 1

sleep(3)

elements = firefox.find_elements("class name", "inhype-grid-post")

for element in elements: print(element.text)

firefox.close()
