import requests
from bs4 import BeautifulSoup
import re
import sys
import os

url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=06460&showNegotiable=true&sortDir=ASC&sourceContext=usedPaidSearchNoZip&distance=50&sortType=DEAL_SCORE'

in_script_body = 'window'

def get_page(url):
    r = BeautifulSoup(requests.get(url).text, 'js.parser')
    return r.text
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def get_listings(page, key):
    listings = page.startswith(key)
    return listings

print(get_listings(get_page(url), in_script_body))