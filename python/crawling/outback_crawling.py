import requests
from bs4 import BeautifulSoup

url = 'https://www.outback.co.kr/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

id_element = soup.find(id='dHead')
print(id_element)
print(id_element.text)
