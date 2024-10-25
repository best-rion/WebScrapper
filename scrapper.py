from bs4 import BeautifulSoup
import random
import json

def getProductList(html_file):
    with open(html_file, 'r') as file:

        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        cards = soup.find_all('div', class_ = 'product-card')

        watches = []

        for card in cards:

            dictionary = {}

            brand =  card.h6.text
            dictionary['brand'] =  brand

            name_tag = card.find('h6', class_ = 'product-name')
            name = name_tag.a.text
            dictionary['name'] = name

            price_tag = card.find('h6', class_ = 'product-price')
            price = price_tag.span.text
            dictionary['price'] = int(price[2:].replace(',',''))

            dictionary['stock'] = random.randint(10,100)

            pic_tag = card.find('a', class_ = 'product-image')
            dictionary['pic_url'] = pic_tag.img['src']


            watches.append(dictionary)
        
        return watches


def writeToJsonFile(html_file):
    jsonContent = json.dumps(getProductList(html_file))

    with open('watches.json', 'w') as file:
        file.write(jsonContent)

writeToJsonFile('index.html')