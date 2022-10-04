import sys
from termcolor import colored

text1 = colored('Hello', 'red', attrs=['bold', 'blink'])
comma = colored(',', 'green', attrs=['bold'])
text2 = colored('World!', 'blue', attrs=['underline'])
fulltext = text1+comma+text2

print(fulltext) # print fulltext in color