import urllib.request
import json

def numberOfCovid():
    lastCovidInquiry = 0
    totalCovidInquiry = 0

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

        lastCovidInquiry = records[int(days) - 1]['帰国者・接触者相談センター相談件数']
        if lastCovidInquiry is None:
            lastCovidInquiry = records[int(days) - 2]['帰国者・接触者相談センター相談件数']

        for index, item in enumerate(records):
            if item['帰国者・接触者相談センター相談件数'] is not None:
                totalCovidInquiry = totalCovidInquiry + item['帰国者・接触者相談センター相談件数']

    return {"lastCovidInquiry": lastCovidInquiry, "totalCovidInquiry": totalCovidInquiry}