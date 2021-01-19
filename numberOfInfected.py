import urllib.request
import json
import datetime

def numberOfInfected():
    countBaby = 0
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

    countBabyLatest = 0
    countChildLatest = 0
    countTeenLatest = 0
    countTwentyLatest = 0
    countThirtyLatest = 0
    countFourtyLatest = 0
    countFiftyLatest = 0
    countSixtyLatest = 0
    countSeventyLatest = 0
    countEightyLatest = 0
    countNinetyLatest = 0

    countMale = 0
    countFemale = 0

    countMaleLatest = 0
    countFemaleLatest = 0

    countLatest = 0
    
    today = str(datetime.date.today() - datetime.timedelta(days=1)) + "T00:00:00"

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
            if item['患者_年代'] == "1歳未満":
                countBaby+=1
                if item['公表_年月日'] == today: countBabyLatest+=1
            elif item['患者_年代'] == "10歳未満":
                countChild+=1
                if item['公表_年月日'] == today: countChildLatest+=1
            elif item['患者_年代'] == "10代":
                countTeen+=1
                if item['公表_年月日'] == today: countTeenLatest+=1
            elif item['患者_年代'] == "20代":
                countTwenty+=1
                if item['公表_年月日'] == today: countTwentyLatest+=1
            elif item['患者_年代'] == "30代": 
                countThirty+=1
                if item['公表_年月日'] == today: countThirtyLatest+=1
            elif item['患者_年代'] == "40代": 
                countFourty+=1
                if item['公表_年月日'] == today: countFourtyLatest+=1
            elif item['患者_年代'] == "50代": 
                countFifty+=1
                if item['公表_年月日'] == today: countFiftyLatest+=1
            elif item['患者_年代'] == "60代": 
                countSixty+=1
                if item['公表_年月日'] == today: countSixtyLatest+=1
            elif item['患者_年代'] == "70代": 
                countSeventy+=1
                if item['公表_年月日'] == today: countSeventyLatest+=1
            elif item['患者_年代'] == "80代": 
                countEighty+=1
                if item['公表_年月日'] == today: countEightyLatest+=1
            elif item['患者_年代'] == "90代": 
                countNinety+=1
                if item['公表_年月日'] == today: countNinetyLatest+=1

            if item['患者_性別'] == "男性":
                countMale+=1
                if item['公表_年月日'] == today: countMaleLatest+=1
            elif item['患者_性別'] == "女性":
                countFemale+=1
                if item['公表_年月日'] == today: countFemaleLatest+=1

            if item['公表_年月日'] == today: countLatest+=1
    
    return { "infected": infected, "countLatest": countLatest, \
            "countBaby": countBaby, "countChild": countChild, "countTeen": countTeen, "countTwenty": countTwenty, \
            "countThirty": countThirty,"countFourty": countFourty, "countFifty": countFifty, "countSixty": countSixty, \
            "countSeventy": countSeventy,"countEighty": countEighty, "countNinety": countNinety, \
            "countBabyLatest": countBabyLatest, "countChildLatest": countChildLatest, "countTeenLatest": countTeenLatest, \
            "countTwentyLatest": countTwentyLatest, "countThirtyLatest": countThirtyLatest, "countFourtyLatest": countFourtyLatest, \
            "countFiftyLatest": countFiftyLatest, "countSixtyLatest": countSixtyLatest, "countSeventyLatest": countSeventyLatest, \
            "countEightyLatest": countEightyLatest, "countNinetyLatest": countNinetyLatest, \
            "countMale": countMale, "countFemale": countFemale, "countMaleLatest": countMaleLatest, "countFemaleLatest": countFemaleLatest }