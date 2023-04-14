# importação do webdriver, que é o que possibilita a implementação para todos
# os principais navegadores da web
from time import sleep
from selenium import webdriver

firefox = webdriver.Firefox()

firefox.get("https://quotes.toscrape.com/")

print(firefox.find_element("class name", "quote").text)

firefox.close()