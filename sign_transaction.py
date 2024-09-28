# AがBにトークンを送信するトランザクションをAだけが作成できるようにする処理
# Aの財産が第三者によって送金されるのを防ぐ

import pandas as pd
import datetime
from ecdsa import SigningKey, SECP256k1
import binascii
import json

secret_key_A_str = "54004d1eb23cd5db63c31c3aec98800d4e7683bcb9cf074d6c966f50c37910a0"
public_key_B_str = "7c2c089c89a32d423bd6bde50f55964a3e21f3a99a6e24c00549d40feda655fe6041cb8476deffb4b6e52f3c191ab3e59c086d6b9ebba099d325c138d9403d58"

# 文字列を秘密鍵オブジェクトに変換するために16進数をバイナリに戻してから秘密鍵を生成
secret_key_A = SigningKey.from_string(binascii.unhexlify(secret_key_A_str), curve=SECP256k1)

# 秘密鍵から公開鍵を生成
public_key_A = secret_key_A.verifying_key
public_key_A_str = public_key_A.to_string().hex()

# 電子署名の対象を作成
# AからBにそうしん
time_now = datetime.datetime.now(datetime.timezone.utc).isoformat()
unsigned_transactions = { "time": time_now, "sender": public_key_A_str, "receiver": public_key_B_str, "amount": 3 }

# トランザクションにAの秘密鍵で署名
signature = secret_key_A.sign(json.dumps(unsigned_transactions).encode('utf-8'))
transaction = { "time": time_now, "sender": public_key_A_str, "receiver": public_key_B_str, "amount": 3, "signature": signature.hex() }

print(transaction)
pd.to_pickle(transaction, "signed_transaction.pkl")