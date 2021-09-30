import json
import requests
from bs4 import BeautifulSoup as bs
    
def scraping(url):
    # urlにRequestを投げる
    response = requests.get(url)
    # requestの内容をパースする
    soup = bs(response.content, 'html.parser')
    # [strogn]タグのテキストを取得
    text = soup.find('strong').text

    return len(str(text))