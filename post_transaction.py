import requests
import pandas as pd
import datetime
from ecdsa import SigningKey, SECP256k1
import binascii
import json

coin_num = 3

# 送信者の秘密鍵と受信者の公開鍵の文字列
secret_key_sender_str = "54004d1eb23cd5db63c31c3aec98800d4e7683bcb9cf074d6c966f50c37910a0"
public_key_receiver_str = "a53ff8e4f29d9b2b1e826637564e33542fbf981b8621c2599d873166e7c434c8"


# 送信者の鍵をバイナリに
secret_key_sender = SigningKey.from_string(binascii.unhexlify(secret_key_sender_str), curve=SECP256k1)


# 送信者の秘密鍵から公開鍵を作成
public_key_sender = secret_key_sender.verifying_key
public_key_sender_str = public_key_sender.to_string().hex()
time_now = datetime.datetime.now(datetime.timezone.utc).isoformat()
unsigned_transactions = {
  "time": time_now,
  "sender": public_key_sender_str,
  "receiver": public_key_receiver_str,
  "amount": coin_num }

signature = secret_key_sender.sign(json.dumps(unsigned_transactions).encode('utf-8'))
transaction = { 
  "time": time_now,
  "sender": public_key_sender_str,
  "receiver": public_key_receiver_str, 
  "amount": coin_num, 
  "signature": signature.hex()
}

# Json形式にした署名済みトランザクションを'/transaction_pool'にPOSTメソッドで送信
res = requests.post("http://3.27.47.0:8000/transaction_pool", json.dumps(transaction))
print(res.text)