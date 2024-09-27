from ecdsa import VerifyingKey, BadSignatureError, SECP256k1
import binascii
import json

class BlockChain(object):
  def __init__(self):
    self.transaction_pool = { "transactions": [] }
  
  def verify_transaction(self, transaction):
    # 送信者の公開鍵をバイナリに
    public_key =  VerifyingKey.from_string(binascii.unhexlify(transaction["sender"]), curve=SECP256k1)
		
		# トランザクションの署名を取得
    signature = binascii.unhexlify(transaction["signature"])
		
		# 署名以外のトランザクション
    unsigned_transactions = { 
			"time": transaction["time"], 
			"sender": transaction["sender"], 
			"receiver": transaction["receiver"], 
			"amount": transaction["amount"] 
		}
		
    try:
			# 送信者の署名を、送信者の公開鍵を使用して検証
      flg = public_key.verify(signature, json.dumps(unsigned_transactions).encode('utf-8'))
      return flg
    except BadSignatureError:
      return False