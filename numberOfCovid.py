import urllib.request
import json

def numberOfCovid():
    covidInquiry = 0

    # 受診・相談センター相談件数
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=b71cdec1-b763-4b67-9ff4-24deaea65a55&limit=1"

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        days = str(data['result']['total'])

    # 日ごとのレコードを全て取得
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=b71cdec1-b763-4b67-9ff4-24deaea65a55&limit=" + days

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        records = data['result']['records']

        for index, item in enumerate(records):
            covidInquiry = covidInquiry + item['帰国者・接触者相談センター相談件数']

    return covidInquiry