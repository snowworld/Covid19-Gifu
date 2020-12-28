import urllib.request
import json

def numberOfInspected():
    lastInspected = 0
    totalInspected = 0

    # 検査実施件数
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=f2468ba2-efe8-483f-9b1b-ee67755dedb0&limit=1"

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        days = str(data['result']['total'])

    # 日ごとのレコードを全て取得
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=f2468ba2-efe8-483f-9b1b-ee67755dedb0&limit=" + days

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        records = data['result']['records']

        lastInspected = records[int(days) - 1]['検査件数']

        for index, item in enumerate(records):
            totalInspected = totalInspected + item['検査件数']
   
    return {"lastInspected": lastInspected, "totalInspected": totalInspected}