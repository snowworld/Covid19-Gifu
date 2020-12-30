import urllib.request
import json

def numberOfDead():
    countSeventy = 0
    countEighty = 0
    countNinety = 0
    countOther = 0

    countMale = 0
    countFemale = 0

    # 死亡患者属性
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=ff0a6fb9-483f-424b-9e68-5aa979af51b8&limit=1"

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        dead = str(data['result']['total'])

    # 死亡者ごとのレコードを全て取得
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=ff0a6fb9-483f-424b-9e68-5aa979af51b8&limit=" + dead

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        records = data['result']['records']

        for index, item in enumerate(records):
            if item['年代'] == "70代": countSeventy+=1
            elif item['年代'] == "80代": countEighty+=1
            elif item['年代'] == "90代": countNinety+=1
            else: countOther+=1

            if item['性別'] == "男性": countMale+=1
            elif item['性別'] == "女性": countFemale+=1

    return { "dead": dead, "countSeventy": countSeventy, "countEighty": countEighty, "countNinety": countNinety, "countOther": countOther, \
            "countMale": countMale, "countFemale": countFemale }