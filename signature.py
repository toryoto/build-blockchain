from ecdsa import SigningKey, BadSignatureError, SECP256k1

# ビットコインと同じ楕円曲線暗号のSECP256k1を使用して秘密鍵の作成
secret_key = SigningKey.generate( curve = SECP256k1 )
print("秘密鍵：" + secret_key.to_string().hex())

# 秘密鍵を使用して公開鍵を生成・取得して16進数で表示
public_key = secret_key.verifying_key
print("公開鍵：" + public_key.to_string().hex())

# 日本語を含む文字列を文字コードutf-8でエンコードしてから電子署名を算出
doc = "これは送信したい文章です"
signature = secret_key.sign(doc.encode('utf-8'))
print("電子署名：" + signature.hex())

# 受け取り側は公開鍵で電子署名が元の文章から作成されたものか検証
try:
  public_key.verify(signature, doc.encode('utf-8'))
  print("文章は改竄されていません")
except BadSignatureError:
  print("文章が改竄されています")