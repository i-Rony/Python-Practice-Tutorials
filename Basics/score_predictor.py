def scorePredictor():
    tOvers=input("Enter total overs :")
    cOver=input("Enter current over :")
    cRuns=input("Enter current score :")

    convertTovers=int(tOvers)
    convertCover=int(cOver)
    convertCruns=int(cRuns)

    runrate=convertCruns/convertCover

    predictor=runrate*convertTovers

    print("\n------------------------")
    print("Run rate :"+str(round(runrate,2)))
    print("Score Predictor :"+str(round(predictor)))
    print("\n------------------------")


scorePredictor()