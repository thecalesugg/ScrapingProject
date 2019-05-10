#Beautiful Soup 4


#import libraries
import urllib.request
from bs4 import BeautifulSoup


quote_page = "https://www.google.com"
page = urllib.request.urlopen(quote_page)
print(page)
soup = BeautifulSoup(page, 'html.parser')

#print(soup.prettify())
print(soup.title)
s = soup.find_all('a')
for i in s:
    print(i.get('href'))



'''
name_box = soup.find_all('h1') #attrs={'class': 'companyName'})
#print(name_box)

name = name_box.text.strip()# strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)
'''