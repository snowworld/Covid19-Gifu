import numberOfInfected, numberOfDead, numberOfInspected, numberOfGeneral, numberOfCovid

def getNumberOf(userText):
    stat = ""

    statInfected = numberOfInfected.numberOfInfected()
    statDead = numberOfDead.numberOfDead()
    statInspected = numberOfInspected.numberOfInspected()
    statGeneral = numberOfGeneral.numberOfGeneral()
    statCovid = numberOfCovid.numberOfCovid()

    if userText == "最新の陽性者数は？":
        stat = f"最新の陽性者数累計は { statInfected['infected'] } 名です。\n\n\
            [内訳]\n\
            10代未満: { statInfected['countChild'] } 名\n\
            10代: { statInfected['countTeen'] } 名\n\
            20代: { statInfected['countTwenty'] } 名\n\
            30代: { statInfected['countThirty'] } 名\n\
            40代: { statInfected['countFourty'] } 名\n\
            50代: { statInfected['countFifty'] } 名\n\
            60代: { statInfected['countSixty'] } 名\n\
            70代: { statInfected['countSeventy'] } 名\n\
            80代: { statInfected['countEighty'] } 名\n\
            90代: { statInfected['countNinety'] } 名\n\n\
            男性: { statInfected['countMale'] } 名\n\
            女性: { statInfected['countFemale'] } 名\n"
    elif userText == "最新の死亡者数は？":
        stat = f"最新の死亡者数累計は { statDead['dead'] } 名です。\n\n\
            [内訳]\n\
            60代: { statDead['countSixty'] } 名\n\
            70代: { statDead['countSeventy'] } 名\n\
            80代: { statDead['countEighty'] } 名\n\
            90代: { statDead['countNinety'] } 名\n\
            100歳以上: { statDead['countHundred'] } 名\n\
            その他: { statDead['countOther'] } 名\n\n\
            男性: { statDead['countMale'] } 名\n\
            女性: { statDead['countFemale'] } 名\n"
    elif userText == "最新の検査数は？":
        stat = f"最新の検査数は { statInspected['lastInspected'] } 件です。\n\
            累計は { statInspected['totalInspected'] } 件です。\n"
    elif userText == "最新の健康相談件数は？":
        stat = f"最新の健康相談件数は { statGeneral['lastGeneralInquiry'] } 件です。\n\
            累計は { statGeneral['totalGeneralInquiry'] } 件です。\n"
    elif userText == "最新のコロナ相談数は？":
        stat = f"最新のコロナ相談件数は { statCovid['lastCovidInquiry'] } 件です。\n\
            累計は { statCovid['totalCovidInquiry'] } 件です。\n"
    else:
        stat = "何かテキストを入力してください。\n下の画面に選択肢が出ます。\n"

    return stat