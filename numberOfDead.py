import urllib.request
import json

# 死亡患者属性
url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=ff0a6fb9-483f-424b-9e68-5aa979af51b8&limit=1"

with urllib.request.urlopen(url) as res:
   data = json.load(res)
   # print(data)
   dead = data['result']['total']
   print(f"死亡者数: {dead} 名")
