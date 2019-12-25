# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
import csv

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 100

page_link = 'https://ethiopiazare.com/amharic/history/history/4379-abuna-theophilos-by-aklilu-habtewold'


with open('results.csv','w') as f:
    f.write('Text')


driver  = webdriver.Firefox()

for i in range(1,MAX_PAGE_NUM+1):
    print('Going Through:',page_link)
    page_num = (MAX_PAGE_DIG)

    driver.get(page_link)
    texts = driver.find_elements_by_tag_name('p')
    

    num_text = len(texts)
    with open('results.csv', 'a') as f:
        for i in range(num_text):
            f.write(texts[i].text.encode('utf-8')+'\n')



    links = driver.find_elements_by_class_name('next')
    page_link = links[0].find_element_by_tag_name('a').get_attribute('href')


driver.close()