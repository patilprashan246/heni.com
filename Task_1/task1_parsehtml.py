#import modules
from lxml import html
import re
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as bs

#get html and tree
html_page_link = '../candidateEvalData/webpage.html'

import re


def clean(price):
    if price is None:
        return ''

    if isinstance(price, str):
        return re.sub(
            r'\s+', ' ',
            price.replace('\xa0', ' ').replace('(', '').replace(')', '').replace(
                'USD', '').replace('GBP', '').replace(',', '').replace('-', ',')).strip()
    price = [clean(c) for c in price]

    return [c for c in price if c]


#
soup = bs(open(html_page_link, encoding='utf-8'), 'lxml')
# parse artist name
artist_Name=soup.find(id='main_center_0_lblLotPrimaryTitle').text.strip().split('(')[0].strip()
#parse painting name
painting_Name=soup.find(id='main_center_0_lblLotSecondaryTitle').text.strip()
#parse price GBP
price_GBP=clean(soup.find(id='main_center_0_lblPriceRealizedPrimary').text.strip())
#parse price US
price_US=clean(soup.find(id='main_center_0_lblPriceRealizedSecondary').text.strip())
#parse price GBP est
price_GBP_est=clean(soup.find(id='main_center_0_lblPriceEstimatedPrimary').text.strip())
#parse price US est
price_US_est=clean(soup.find(id='main_center_0_lblPriceEstimatedSecondary').text.strip())
#image link
image_Link=soup.find(id='imgLotImage').get('src')
#sale_Date
sale_Date=datetime.strptime(soup.find(id='main_center_0_lblSaleDate').text.strip().replace(',', ''),'%d %B %Y').strftime('%Y-%m-%d')

christies_df = pd.DataFrame(
    [[artist_Name, painting_Name, price_GBP, price_US, price_GBP_est, price_US_est, image_Link]],
    columns=['Artist', 'Painting', 'Price GBP', 'Price US', 'Price GBP Est ', 'Price US Est', 'Image'],
)

print(christies_df.head())