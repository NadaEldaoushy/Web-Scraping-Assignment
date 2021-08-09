import requests
import csv
from bs4 import BeautifulSoup

with open ('booksScraping.csv','w') as f:
    write=csv.DictWriter(f,fieldnames=['title','price','rating'])
    write.writeheader()

    url = 'http://books.toscrape.com/catalogue/category/books/science_22/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    x=soup.find_all('article', attrs = {'class','product_pod'})
    for i in range(14):
        title=x[i].find('h3').find('a').attrs['title']
        price = x[i].find('p', attrs={'class': 'price_color'}).get_text()
        price1=price.split('Â')[1]
        rating=x[i].find('p').attrs['class'][1]
        write.writerow({'title': title,'price': price1 , 'rating' : rating})   


