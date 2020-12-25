import urllib.request
import json

generalInquiry = 0

# 健康相談窓口相談件数
url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=aa3ebb23-5704-470f-a41e-d834d0a51fc0&limit=1"

with urllib.request.urlopen(url) as res:
   data = json.load(res)
   # print(data)
   days = str(data['result']['total'])


# 日ごとのレコードを全て取得
url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=aa3ebb23-5704-470f-a41e-d834d0a51fc0&limit=" + days

with urllib.request.urlopen(url) as res:
   data = json.load(res)
   records = data['result']['records']

   for index,item in enumerate(records):
      generalInquiry = generalInquiry + item['相談件数']
      

print(f"相談件数: {generalInquiry} 件")
