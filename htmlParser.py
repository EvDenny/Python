import os, sys, bs4, requests, html5lib, urlopen, urllib.request, types

# HTMLParser Class Attempt
class HTMLParser(URL):
    def __init__(self, URL):
        self.URL = URL
        self.request = requests.get(URL)
    
    def parse(self, parser, library):
        if (parser == BS4):
            self.soup = bs4.BeautifulSoup(self.request.text, library)
        else:
            error('INVALID PARSER SELECTED')
    
    def soupData(self, soup, value):
        for item in self.soup(value):
            print(item)
    
    def getData(self, soup, value, param1=None, param2=None):
        if (param1 != None):
            if (param2 != None):
                self.soupData = self.soup.param1.param2
                for item in self.soup.param1.param2(value):
                    print(item)
            else:
                self.soupData = self.soup.param1
                for item in self.soup.param1(value):
                    print(item)
        else:
            self.soupData = self.soup
            for item in self.soup(value):
                print(item)

parser = HTMLParser(url)

parser.parse(BS4, 'html5lib')
parser.getData(soup, 'input', body, form)