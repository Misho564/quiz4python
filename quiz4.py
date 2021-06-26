import requests
from bs4 import BeautifulSoup

file = open('products.csv', 'w', encoding='utf-8_sig')
header = 'titles,prices,monthly price, shipping \n'
file.write(header)

for i in range(1, 13):
    url = requests.get(
        'https://vendoo.ge/c/technics/kompiuteruli-teqnika/noutbuqebi-da-misi-aqsesuarebi?page=' + str(i))

    content = url.text
    soup = BeautifulSoup(content, 'html.parser')
    catalog = soup.find('div', {'class': 'catalog-page__content'})

    info = catalog.find_all('div', {'class': 'product__info'})

    for each in info:
        title_divs = each.find('div', {'class': 'product__title'})
        titles = title_divs.text
        price = each.span.text.strip()
        monthly = each.find('span', {'class': 'product__installment'})
        monthly_price = monthly.text.strip()
        shipping = each.find('span', {'class': 'product__shipping'})
        try:
            shipping_details = shipping.span.text.strip()
        except AttributeError:
            pass
        file.write(titles + ',' + '  ' + price + ',' + '  ' + monthly_price + ',' + '  ' + shipping_details + '\n')
