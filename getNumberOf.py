import numberOfInfected, numberOfDead, numberOfInspected, numberOfGeneral, numberOfCovid

def getNumberOf(userText):

    if userText == "最新の感染者数は？": stat = f"最新の感染者数累計は { numberOfInfected.numberOfInfected() } 件です。\n"
    elif userText == "最新の死亡者数は？": stat = f"最新の死亡者数累計は { numberOfDead.numberOfDead() } 件です。\n"
    elif userText == "最新の検査数は？":
        stat = f"最新の検査数は { numberOfInspected.numberOfInspected()['lastInspected'] } 件です。\n累計は { numberOfInspected.numberOfInspected()['totalInspected'] } 件です。\n"
    elif userText == "最新の健康相談件数は？":
        stat = f"最新の健康相談件数は { numberOfGeneral.numberOfGeneral()['lastGeneralInquiry'] } 件です。\n累計は { numberOfGeneral.numberOfGeneral()['totalGeneralInquiry'] } 件です。\n"
    elif userText == "最新のコロナ相談数は？":
        stat = f"最新のコロナ相談件数は { numberOfCovid.numberOfCovid()['lastCovidInquiry'] } 件です。\n累計は { numberOfCovid.numberOfCovid()['totalCovidInquiry'] } 件です。\n"

    return stat