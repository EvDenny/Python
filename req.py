import os, sys, bs4, requests, types
import html5lib, urlopen, urllib.request

url = "http://www.google.com/" # URL for scraping
request = requests.get(url) # Gets request from URL
# request contains the request from the url
# If we print(request) we will return the statusCode of '200'
# Conirming that the request was successful and we can begin
# parsing the info using BS4 to return useful information

# Use BS4 (BeautiulSoup4) to decode the html request into text
soup = bs4.BeautifulSoup(request.text, 'html5lib')
###print(soup.body.form) COMMENTED OUT FOR READABILITY

# This code returns each item in the form we parsed and 
# shows us where the input sections are and their names
# and values.
for item in soup.body.form('input'):
    print(item)

# From the form('input') info, we can see that the search
# box has the title="Google Search", and a value="". The
# input class="lsb" name="btnG" type="submit" value="Google
# Search" submits the info from the text box into a Google
# Search. There are some hidden input values that could be
# interesting to explore, however, these should be the targets
# for POSTing search info into Google.

# There's also an input name-"iflsig" with SHA1(or SHA something)
# encoding. 
# <input name="iflsig" type="hidden" value="AJiK0e8AAAAAYzuwcT5388mU3B9_fqbNCCNrv3A1KVgc"/>