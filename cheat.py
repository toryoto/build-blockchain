import pandas as pd

transaction = pd.read_pickle("signed_transaction.pkl")
print("改竄前のトランザクション")
print(transaction)

transaction = {
	"time": transaction["time"],
  "sender": transaction["sender"],
  "receiver": transaction["receiver"],
  "amount": 30,
  "signature": transaction["signature"]
}
print("改竄後のトランザクション")
print(transaction)
pd.to_pickle(transaction, "signed_transaction.pkl")

# 改ざんがばれる理由
# 1. デジタル署名は以下のようにトランザクションの内容に基づいて生成される
# signature = secret_key_A.sign(json.dumps(unsigned_transactions).encode('utf-8'))
# 2. トランザクションの内容が変更されると、元の署名と一致しなくなる
# 3. 署名の検証時に、トランザクションの内容と署名が一致しないため、改ざんが検出される