from bs4 import BeautifulSoup
import requests

web_link = "https://dailyinjera.org/series"


source = requests.get(web_link).text

soup = BeautifulSoup(source,'lxml')

article = soup.find('div',class_='sppb-content-holder')

headline = article.h3.text
content = article.find('p',class_='p1').text

print(headline)
print()
print(content)
# sppb-content-holder