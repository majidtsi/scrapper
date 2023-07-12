import requests
from bs4 import BeautifulSoup as bss4
import csv
url = requests.get("https://www.amazon.eg/s?bbn=21832872031&rh=n%3A18018102031%2Cn%3A21832872031%2Cn%3A21832915031&dc&qid=1689107808&rnid=21832872031&ref=lp_21832872031_nr_n_0")
#https://deals.souq.com/eg-ar/smart-tvs/c/15236
print(url)
soup=bss4(url.text, 'lxml')
#product_title=soup.findAll('span',{'class':'a-color-base'})
#print(product_title)
products=soup.findAll('div',{'class':'octopus-pc-item-block'})
with open('../products.csv', 'w', encoding='utf-8', newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Product Name','Price'])
    for product in products:
        title=product.find('span','a-color-base').text
        price=product.find('div','octopus-pc-asin-price-section')
        writer.writerow([title,price])
    print("done")