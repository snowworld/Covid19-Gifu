import numberOfInfected, numberOfDead, numberOfInspected, numberOfGeneral, numberOfCovid

def getNumberOf():
    infected = numberOfInfected.numberOfInfected()
    dead = numberOfDead.numberOfDead()
    inspected = numberOfInspected.numberOfInspected()
    generalInquiry = numberOfGeneral.numberOfGeneral()
    covidInquiry = numberOfCovid.numberOfCovid()

    numbersJson = {
        "infected": infected,
        "dead": dead,
        "inspected": inspected,
        "generalInquiry": generalInquiry,
        "covidInquiry": covidInquiry
    }

    return numbersJson