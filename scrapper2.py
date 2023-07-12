"""Abdelmajid Mamar"""
"""Programma scrapper con request-html"""
#pip install requests-html
import csv
from requests_html import HTMLSession

#/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[2]/ul/li[1]
session = HTMLSession()
url = session.get("https://www.amazon.eg/-/en/%D8%AA%D9%84%D9%81%D8%B2%D9%8A%D9%88%D9%86%D8%A7%D8%AA/b/?ie=UTF8&node=21832982031&ref_=sv_sv_elec_all_4")
#url.html.render(sleep=2)
products=url.html.xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[1]')

with open('../products.csv', 'w', encoding='utf-8', newline="") as file:
    writer=csv.writer(file)
    writer.writerow(['Product Name','Price','Description','Rate'])
    for product in products.absolute_links:
        url = session.get(product)
        name = url.html.find('h1#title',first=True).text
        price=url.html.find('h3.price',first=True).text
        description=url.html.find('div.item-details-mini',first=True).text
        rate=url.html.find('div.avg',first=True).text
        writer.writerow([name,price,description,rate])

print("Done")
