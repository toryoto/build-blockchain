from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import blockchain

class Transaction(BaseModel):
  time: str
  sender: str
  receiver: str
  amount: int
  signature: str

transaction_pool = { "transactions": [] }
app = FastAPI()

@app.get("/transaction_pool")
def get_transaction_pool():
  return transaction_pool

@app.post("/transaction_pool")
def post_transaction(transaction :Transaction):
  print(transaction)
  transation_dict = transaction.dict()
  if blockchain.verify_transaction(transation_dict):
    transaction_pool["transactions"].append(transation_dict)
    return { "message": "Transaction is posted" }
  
  
if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000)
    