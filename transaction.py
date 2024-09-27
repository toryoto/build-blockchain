import datetime

time_now = datetime.datetime.now(datetime.timezone.utc).isoformat()
transaction1 = { "time": time_now, "sender": "C", "receiver": "D", "amount": 1 }

time_now = datetime.datetime.now(datetime.timezone.utc).isoformat()
transaction2 = { "time": time_now, "sender": "D", "receiver": "C", "amount": 3 }

transaction = [ transaction1, transaction2 ]
print(transaction)