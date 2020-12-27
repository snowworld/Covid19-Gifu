import urllib.request
import json

def numberOfInfected():
   # 陽性患者属性
   url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=9c35ee55-a140-4cd8-a266-a74edf60aa80&limit=1"

   with urllib.request.urlopen(url) as res:
      data = json.load(res)
      # print(data)
      infected = data['result']['total']
   
   return infected