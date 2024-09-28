# 既存のトランザクションをコピーしてそのまま送る処理
import requests
import json

path = "http://3.27.47.0:8000/transaction_pool"
res = requests.get(path)
transactions_dict = res.json()
received_transaction = transactions_dict["transactions"][0]

res = requests.post(path, json.dumps(received_transaction))
print(res.text)