import os
import time
import json
import requests
import jwt
from dotenv import load_dotenv


# .envファイルをロードして環境変数に反映、環境変数からローカル変数に読み込む
load_dotenv()
ZOOM_API_KEY = os.getenv('ZOOM_API_KEY')
ZOOM_API_SECRET = os.getenv('ZOOM_API_SECRET')

# JWTトークンを生成
jwt_payload = {
    "iss": ZOOM_API_KEY,
    "exp": int(time.time()) + 900
}
encoded_jwt = jwt.encode(jwt_payload, ZOOM_API_SECRET, algorithm="HS256")

# APIアクセス: /usersにアクセス
url = "https://api.zoom.us/v2/users?page_size=300"
response = requests.get(url, headers={"Authorization" : f'Bearer {encoded_jwt}'})

# responseオブジェクトに変換
response_obj = response.json()  # json()とかいうメソッド割に出来上がるのはオブジェクト(dict)
response_json = json.dumps(response_obj)

# ファイルに出力
with open('output.json', 'w', encoding='utf-8') as f:
    print(response_json, file=f)