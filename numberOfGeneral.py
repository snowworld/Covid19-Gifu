import urllib.request
import json

def numberOfGeneral():
    lastGeneralInquiry = 0
    totalGeneralInquiry = 0

    # 健康相談窓口相談件数
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=aa3ebb23-5704-470f-a41e-d834d0a51fc0&limit=1"

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        days = str(data['result']['total'])

    # 日ごとのレコードを全て取得
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=aa3ebb23-5704-470f-a41e-d834d0a51fc0&limit=" + days

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        records = data['result']['records']

        lastGeneralInquiry = records[int(days) - 1]['相談件数']
        if lastGeneralInquiry is None:
            lastGeneralInquiry = records[int(days) - 2]['相談件数']

        for index, item in enumerate(records):
            if item['相談件数'] is not None:
                totalGeneralInquiry = totalGeneralInquiry + item['相談件数']
         
    return {"lastGeneralInquiry": lastGeneralInquiry, "totalGeneralInquiry": totalGeneralInquiry}