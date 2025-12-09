import funk.boker as boker

Biblotek = boker.Biblotek("Bjarne's store biblotek", "Skien")

run = True


while run:
    x = input()
    if x == "exit":
        run = False
        break
    if x == "legg til":
        print("velg sjanger (fagbok eller literatur)")
        boktypInput = input()
        if boktypInput == "fagbok":
            print("legg til bok med titel, forfater, isbn, fag")
            # data 0:titel 1:forfater 2:isbn: 3:fag
            input_data = str(input())
            data = input_data.split(",")
            forfater_fins = False
            for i in data:
                print(i , "sd")
            for forfater in Biblotek.forfater:
                if data[1] == forfater:
                    forfater_fins = True
                    data[1] = forfater
            if forfater_fins:
                bok = boker.Fagbok(data[0],data[1].navn,data[2],data[3],"fagbok")
            else:
                nyeforfater = boker.Forfater(data[1])
                Biblotek.forfater.append(nyeforfater)
                bok = boker.Fagbok(data[0],nyeforfater,data[2],data[3])
                
                
        print(Biblotek.forfater)
        print(Biblotek.boker)
                
                    
                