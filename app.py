from flask import Flask
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route("/rate")
def liverate():
  response = requests.get("http://www.kjpl.in/")
  soap = BeautifulSoup(response.text,'html.parser')
  gold_rate = soap.find('table',class_="table mjdmahead hidden-sm").find_all('td',class_="gold")
  response = {}
  for rate in gold_rate:
    gold = rate.find('span',class_="gold-rate").find_next(text=True).strip()
    response["Gold 1GM 22CT"] = gold
    
  silver_rate = soap.find('table',class_="table mjdmahead hidden-sm").find_all('td',class_="silver")
  for rate in silver_rate:
    silver = rate.find('span',class_="silver-rate").find_next(text=True).strip()
    response["SILVER 1GM"] = silver
  return response

if __name__ == '__main__':
  app.run()