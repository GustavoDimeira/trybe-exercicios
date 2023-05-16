from parsel import Selector
import requests

URL_BASE = "https://api.github.com/users"

response = requests.get(URL_BASE)

selector = Selector(text=response.text).get()

print(selector)