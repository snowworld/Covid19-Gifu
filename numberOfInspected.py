import urllib.request
import json

def numberOfInspected():
   inspected = 0

   # 検査実施件数
   url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=f2468ba2-efe8-483f-9b1b-ee67755dedb0&limit=1"

   with urllib.request.urlopen(url) as res:
      data = json.load(res)
      # print(data)
      days = str(data['result']['total'])


   # 日ごとのレコードを全て取得
   url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=f2468ba2-efe8-483f-9b1b-ee67755dedb0&limit=" + days

   with urllib.request.urlopen(url) as res:
      data = json.load(res)
      records = data['result']['records']

      for index, item in enumerate(records):
         inspected = inspected + item['検査件数']
   
   return inspected