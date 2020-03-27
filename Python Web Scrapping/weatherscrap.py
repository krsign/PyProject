import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xn2tgNMzY1I')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id = 'seven-day-forecast-body')
items = week.find_all(class_ = 'tombstone-container')

# get_text() is predefined object
# print(items[0].find(class_ = 'period-name').get_text())
# print(items[0].find(class_ = 'short-desc').get_text())
# print(items[0].find(class_ = 'temp').get_text())

period_name = [item.find(class_ = 'period-name').get_text() for item in items]
short_description = [item.find(class_ = 'short-desc').get_text() for item in items]
temperature = [item.find(class_ = 'temp').get_text() for item in items]

weathers_details = pd.DataFrame(
    {
        'period': period_name,
        'short_ description': short_description,
        'temperature': temperature
    }
) 
print(weathers_details)
weathers_details.to_csv('weather.csv')

