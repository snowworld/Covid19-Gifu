import urllib.request
import json

def numberOfInfected():
    countChild = 0
    countTeen = 0
    countTwenty = 0
    countThirty = 0
    countFourty = 0
    countFifty = 0
    countSixty = 0
    countSeventy = 0
    countEighty = 0
    countNinety = 0

    countMale = 0
    countFemale = 0

    # 陽性患者属性
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=9c35ee55-a140-4cd8-a266-a74edf60aa80&limit=1"

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        infected = str(data['result']['total'])

    # 死亡者ごとのレコードを全て取得
    url = "https://gifu-opendata.pref.gifu.lg.jp/api/3/action/datastore_search?resource_id=9c35ee55-a140-4cd8-a266-a74edf60aa80&limit=" + infected

    with urllib.request.urlopen(url) as res:
        data = json.load(res)
        records = data['result']['records']

        for index, item in enumerate(records):
            if item['患者_年代'] == "10歳未満": countChild+=1
            elif item['患者_年代'] == "10代": countTeen+=1
            elif item['患者_年代'] == "20代": countTwenty+=1
            elif item['患者_年代'] == "30代": countThirty+=1
            elif item['患者_年代'] == "40代": countFourty+=1
            elif item['患者_年代'] == "50代": countFifty+=1
            elif item['患者_年代'] == "60代": countSixty+=1
            elif item['患者_年代'] == "70代": countSeventy+=1
            elif item['患者_年代'] == "80代": countEighty+=1
            elif item['患者_年代'] == "90代": countNinety+=1

            if item['患者_性別'] == "男性": countMale+=1
            elif item['患者_性別'] == "女性": countFemale+=1

    return { "infected": infected, "countChild": countChild, "countTeen": countTeen, "countTwenty": countTwenty, "countThirty": countThirty, \
            "countFourty": countFourty, "countFifty": countFifty, "countSixty": countSixty, "countSeventy": countSeventy, "countEighty": countEighty, \
            "countNinety": countNinety, "countMale": countMale, "countFemale": countFemale }