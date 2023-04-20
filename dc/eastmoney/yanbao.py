import requests
from bs4 import BeautifulSoup

url = 'https://so.eastmoney.com/yanbao/s?keyword=%E5%8C%BB%E7%96%97'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

while url:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div',class_='notice_item')

    for article in articles:
        title = article.text
        link = article['href']
        print(title, link)

    next_page = soup.select_one('div.pagination a[title="下一页"]')
    if next_page:
        url = next_page['href']
    else:
        url = None
