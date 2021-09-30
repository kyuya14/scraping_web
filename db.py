import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('scraping_table')

def db_get():
    res = table.scan()
    return res['Items'][0]['length']
    
def db_put(value):
    item = {
        "length":value,
        "date":str(datetime.datetime.today())
    }
    table.put_item(Item = item)
    
    