import requests
import pandas as pd
import datetime
from ecdsa import SigningKey, SECP256k1
import binascii
import json

coin_num = 5

# 送信者の秘密鍵と受信者の公開鍵の文字列
secret_key_sender_str = "8dab078a7022bd5527ad29f9b255d4b5991f891f37000e4a3f865cbc5e00621e"
public_key_receiver_str = "1f81cd8e0f25e0691153bafec0ba9db8735d7a82b3d62ef99248c4ba82d9cd150a94b0141903e9462d0b076974f3e5c53fc5a6c61481439dea58931bb125a2a7"


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
res = requests.post("http://127.0.0.1:8001/transaction_pool", json.dumps(transaction))
print(res.text)