import numberOfInfected, numberOfDead, numberOfInspected, numberOfGeneral, numberOfCovid

def getNumberOf(userText):

    if userText == "最新の感染者数は？": stat = f"最新の感染者数は { numberOfInfected.numberOfInfected() } 件です。"
    elif userText == "最新の死亡者数は？": stat = f"最新の死亡者数は { numberOfDead.numberOfDead() } 件です。"
    elif userText == "最新の検査数は？": stat = f"最新の検査数は { numberOfInspected.numberOfInspected() } 件です。"
    elif userText == "最新の健康相談件数は？": stat = f"最新の健康相談件数は { numberOfGeneral.numberOfGeneral() } 件です。"
    elif userText == "最新のコロナ相談数は？": stat = f"最新のコロナ相談件数は { numberOfCovid.numberOfCovid() } 件です。"

    return stat