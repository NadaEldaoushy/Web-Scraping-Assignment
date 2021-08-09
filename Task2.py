import requests
from bs4 import BeautifulSoup


url = 'https://www.exchangerates.org.uk/Dollars-to-Egyptian-Pounds-currency-conversion-page.html'
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')


value=soup.find('span',attrs={'id':'shd2a'}).find('span').getText()
usd_value=input("Enter Value in Dollars: ")
egp_value=float(usd_value)*float(value)


print(egp_value)