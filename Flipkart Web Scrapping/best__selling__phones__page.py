# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup

# For Page1
response = requests.get('https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters')
soup = BeautifulSoup(response.content , 'html.parser')
names = []
prices = []
ratings = []

for i in range(1,51):
    link = soup.find('a', text = 'Next').get('href')
    homepage_link = 'https://www.flipkart.com'

    next_page_link = homepage_link + link[:-1] + str(i)
    
    response2 = requests.get(next_page_link)
    soup2 = BeautifulSoup(response.content , 'html.parser')



    cards = soup2.find_all('div', attrs = {'class':'_1UoZlX'})

    for card in cards:
        name = card.find('div', attrs = {'class':'_3wU53n'})
        price = card.find('div', attrs = {'class':'_2rQ-NK'})
        rating = card.find('div', attrs = {'class':'hGSR34'})
        
        if name:
            name_text = name.text
        else:
            name_text = None
            
        if price:
            price_text = price.text
        else:
            price_text = None
            
        if rating:
            rating_text = rating.text
        else:
            rating_text = None
             
        print('{} {} {}'.format(name_text, price_text, rating_text+' ⭐️'))
        names.append(name_text)
        prices.append(price_text)
        ratings.append(rating_text)
        
mobile_price_rating = pd.DataFrame(
    {'Mobile': names,
     'Price' : prices,
     'Ratings':ratings,
     })

mobile_price_rating.to_csv('flipkart_data.csv')
