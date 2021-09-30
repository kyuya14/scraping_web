import json
import requests
from bs4 import BeautifulSoup as bs
import scraping
import db
import line_send

def lambda_handler(event, context):
    url = 'https://showakinenpark.resv.jp/'
    # TODO implement
    new_len = scraping.scraping(url)    # 新しい文字数を取得
    old_len = db.db_get()               # 古い文字数を取得
    print(new_len)
    print(old_len)
    
    if old_len == new_len:
        print('nothing to do ')
        db.db_put(new_len)
    else:
        print('line push')
        line_send.send()