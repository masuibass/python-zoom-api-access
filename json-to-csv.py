import json
import csv


# JSONファイルからオブジェクトへ変換 
with open('output.json', 'r') as f:
    response_json = f.read()
response_obj = json.loads(response_json)

# オブジェクトからusersを取り出して、必要な部分だけマップ
users = response_obj['users']
mapper = lambda user: {
    'id': user['id'],
    'first_name': user['first_name'],
    'last_name': user['last_name'],
    'email': user['email'],
}
mapped_users = list(map(mapper, users))

# CSVファイルに書き出し
with open('output.csv', 'w') as f:
    # CSVのフォーマットを決める
    csv.register_dialect('my_dialect', doublequote=True, quoting=csv.QUOTE_ALL)
    # オブジェクトからCSVに一行書き込むwriterを設定する
    writer = csv.DictWriter(f, fieldnames=mapped_users[0].keys(), dialect='my_dialect')
    # 1行目（ヘッダーを書き込む）
    writer.writeheader()
    # mapped_usersでループを回して、1行ずつ書き込む
    for user in mapped_users:
        writer.writerow(user)