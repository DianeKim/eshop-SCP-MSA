from flask import Flask
import requests, random, os

_url_productservice = os.environ.get("URL_PRODUCTSERVICE", default='http://localhost:8080/')

app = Flask(__name__)

@app.route("/api/recommends", methods=['GET'])
def recommend():
  # 상품 목록을 조회한다.
  response = requests.get(_url_productservice + "/api/products")
  products = response.json()
  # 랜덤한 4개의 상품을 추천한다.
  recommendations = { 'recommendations': random.sample(products['products'], 4)}
  print("recommendations : {}".format(recommendations))
  return recommendations
