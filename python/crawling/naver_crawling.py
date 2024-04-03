import requests
from bs4 import BeautifulSoup

URL = 'https://n.news.naver.com/mnews/article/079/0003800908?sid=105'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

headline = soup.select('.media_end_head_headline')
print(headline) 

