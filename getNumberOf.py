import numberOfInfected, numberOfDead, numberOfInspected, numberOfGeneral, numberOfCovid

def getNumberOf(userText):
    stat = ""

    if userText == "最新の陽性者数は？":
        stat = f"最新の陽性者数累計は { numberOfInfected.numberOfInfected()['infected'] } 件です。\n\n\
            [内訳]\n\
            10代未満: { numberOfInfected.numberOfInfected()['countChild'] } 名\n\
            10代: { numberOfInfected.numberOfInfected()['countTeen'] } 名\n\
            20代: { numberOfInfected.numberOfInfected()['countTwenty'] } 名\n\
            30代: { numberOfInfected.numberOfInfected()['countThirty'] } 名\n\
            40代: { numberOfInfected.numberOfInfected()['countFourty'] } 名\n\
            50代: { numberOfInfected.numberOfInfected()['countFifty'] } 名\n\
            60代: { numberOfInfected.numberOfInfected()['countSixty'] } 名\n\
            70代: { numberOfInfected.numberOfInfected()['countSeventy'] } 名\n\
            80代: { numberOfInfected.numberOfInfected()['countEighty'] } 名\n\
            90代: { numberOfInfected.numberOfInfected()['countNinety'] } 名\n\n\
            男性: { numberOfInfected.numberOfInfected()['countMale'] } 名\n\
            女性: { numberOfInfected.numberOfInfected()['countFemale'] } 名\n"
    elif userText == "最新の死亡者数は？":
        stat = f"最新の死亡者数累計は { numberOfDead.numberOfDead()['dead'] } 名です。\n\n\
            [内訳]\n\
            70代: { numberOfDead.numberOfDead()['countSeventy'] } 名\n\
            80代: { numberOfDead.numberOfDead()['countEighty'] } 名\n\
            90代: { numberOfDead.numberOfDead()['countNinety'] } 名\n\
            その他: { numberOfDead.numberOfDead()['countOther'] } 名\n\n\
            男性: { numberOfDead.numberOfDead()['countMale'] } 名\n\
            女性: { numberOfDead.numberOfDead()['countFemale'] } 名\n"
    elif userText == "最新の検査数は？":
        stat = f"最新の検査数は { numberOfInspected.numberOfInspected()['lastInspected'] } 件です。\n\
            累計は { numberOfInspected.numberOfInspected()['totalInspected'] } 件です。\n"
    elif userText == "最新の健康相談件数は？":
        stat = f"最新の健康相談件数は { numberOfGeneral.numberOfGeneral()['lastGeneralInquiry'] } 件です。\n\
            累計は { numberOfGeneral.numberOfGeneral()['totalGeneralInquiry'] } 件です。\n"
    elif userText == "最新のコロナ相談数は？":
        stat = f"最新のコロナ相談件数は { numberOfCovid.numberOfCovid()['lastCovidInquiry'] } 件です。\n\
            累計は { numberOfCovid.numberOfCovid()['totalCovidInquiry'] } 件です。\n"
    else:
        stat = "何かテキストを入力してください。\n下の画面に選択肢が出ます。\n"

    return stat