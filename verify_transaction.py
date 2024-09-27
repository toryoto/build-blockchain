import pandas as pd
from ecdsa import VerifyingKey, BadSignatureError, SECP256k1
import binascii
import json

# 署名されたトランザクションを読み込む
transaction = pd.read_pickle("signed_transaction.pkl")

# トランザクションからAの公開鍵を取得
public_key_A = VerifyingKey.from_string(binascii.unhexlify(transaction["sender"]), curve=SECP256k1)

# トランザクションの署名を取得
signature = binascii.unhexlify(transaction["signature"])

# 検証用の署名されていないトランザクションデータを作成
unsigned_transaction = {
	"time": transaction["time"],
  "sender": transaction["sender"],
  "receiver": transaction["receiver"],
  "amount": transaction["amount"]
}

try:
	# 署名を検証
	# 改ざんされていたら元の署名と一致しなくなる
  public_key_A.verify(signature, json.dumps(unsigned_transaction).encode('utf-8'))
  print("トランザクションは改竄されていません")
except BadSignatureError:
  print("トランザクションが改竄されています")