import json
import requests
import boto3
    
def send():
    # send message to LINE
    api_url = "https://notify-api.line.me/api/notify"      # apiurl
    access_token = get_parameters("LINE_TOKEN")            # LINE_TOKEN ssmより取得
    message = "please check BBQ site."
    headers = {'Authorization': 'Bearer ' + access_token}
    payload = {'message': message}
    
    # postを実行してLINEを送信する
    res = requests.post(api_url, headers=headers, params=payload)

def get_parameters(param_key):
    # get value from SSM parameterStore
    REGION = "ap-northeast-1"
    ssm = boto3.client('ssm', region_name=REGION)
    response = ssm.get_parameters(
        Names=[
            param_key,
        ],
        WithDecryption=True
    )
    return response['Parameters'][0]['Value']