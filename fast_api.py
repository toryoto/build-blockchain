from fastapi import FastAPI
import uvicorn

app = FastAPI()

# ルートパスにアクセスされた時に実行するメソッド
@app.get("/")
def index():
  return "Hello!"

# サーバを起動
if __name__ == "__main__":
  uvicorn.run("fast_api:app", host="0.0.0.0", port=8000)