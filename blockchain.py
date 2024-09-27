from ecdsa import VerifyingKey, BadSignatureError, SECP256k1
import binascii
import json
import pandas as pd
import os

TRANSACTIO_FILE = "./transaction_data.pkl"

class BlockChain(object):
	def __init__(self):
		self.transaction_pool = {"transactions": []}

	def save_transaction_pool(self):
		pd.to_pickle(self.transaction_pool, TRANSACTIO_FILE)

	def load_transaction_pool(self):
		if os.path.isfile(TRANSACTIO_FILE):
			transaction_data = pd.read_pickle(TRANSACTIO_FILE)
			return transaction_data
		else:
			return {"transaction": []}

	def add_transaction_pool(self, transaction):
		# 送信するトランザクションがすでに存在しない場合は追加
		if transaction not in self.transaction_pool["transaction"]:
			self.transaction_pool["transactions"].append(transaction)
			return True
		else:
			return False

	def verify_transaction(self, transaction):
		# 送金額がマイナスはFalse
		if transaction["amount"] < 0:
			return False

		# 送信者の公開鍵をバイナリに
		public_key = VerifyingKey.from_string(binascii.unhexlify(transaction["sender"]), curve=SECP256k1)

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