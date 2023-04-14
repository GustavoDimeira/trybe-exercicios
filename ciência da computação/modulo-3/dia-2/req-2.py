# importação do webdriver, que é o que possibilita a implementação para todos
# os principais navegadores da web
from time import sleep
from selenium import webdriver

firefox = webdriver.Firefox()

url = "https://www.wikimetal.com.br/iron-maiden-scorpions-kiss-veja-melhores-albuns-1982/"

firefox.get(url)

rank = firefox.find_element("id", "polls-151").find_elements("tag name", "li")

for item in rank:
    print(item.text.split(" - ")[0], ": ", item.text.split("%, ")[1].split(" V")[0])

firefox.close()