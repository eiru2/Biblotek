class Biblotek:
    def __init__(self, navn:str, plass:str):
        """_summary_

        Args:
            navn (str): navn po biblotek
            plass (str): hvor det befiner
        """
        self.navn = navn
        self.plass = plass
        # self.boker = [[],[]] # index 0 for fag og index 1 er for litertur
        self.boker = []
        self.bokDict = {}
        
        self.forfater = []
        
        self.personer = []
        self.personDict = {}
        
    def leggTilBok(self,bok):
        """_summary_

        Args:
            bok (class): legg er til bok i en liste
        """
        self.boker.append(bok)
        
        # print(self.boker)
    
    def get_bokDict(self):
        """_summary_
            lagger en ordbok med isbn som nøkel
        """
        self.bokDict = {}
        for i in range(len(self.boker)):
            tempDict = {}
            tempDict["titel"] = self.boker[i].titel
            tempDict["forfater"] = self.boker[i].forfater
            tempDict["isbn"] = self.boker[i].isbn
            tempDict["utlont"] = self.boker[i].utlont
            tempDict["boktype"] = self.boker[i].boktype
            tempDict["fag_sjanger"] = self.boker[i].fag_sjanger
            tempDict["id"] = i
            self.bokDict[str(self.boker[i].isbn)] = tempDict
        # print(self.bokDict)

    
    def leggTilforfater(self,forfater):
        """_summary_

        Args:
            forfater (class): legger til en forafter i en liste
        """
        self.forfater.append(forfater)
        
   
    def leggTilpersoner(self,person):
        """_summary_

        Args:
            forfater (class): legger til en person i en liste
        """
        
        self.personer.append(person)
        
    def get_personDict(self):
        """_summary_
            lagger en ordbok med personer
        """
        self.personDict = {}
        for i in range(len(self.personer)):
            tempDict = {}
            tempDict["navn"] = self.personer[i].navn
            isbn_list = []
            tempDict["boker"] = self.personer[i].boker
            tempDict["id"] = i
            self.personDict[str(self.personer[i].navn)] = tempDict

        print(self.personDict)
        
            

class Bok:
    def __init__(self, titel:str, forfater:str, isbn:int, boktype:str, fag_sjanger:str, utlont:bool = False):
        """_summary_
            en bok class som hold på bok verdier
        Args:
            titel (str): Navn po boken
            forfater (str): forfater po boken
            isbn (int): registrerings number til boken
            boktype (str): om det er en faglig boke eller en literatur
            fag_sjanger (str): sjanger eller hvilket fag
            utlont (bool, optional): om den er ut lont. Defaults to False.
        """
        self.titel = titel
        self.forfater = forfater
        self.isbn = isbn
        self.utlont = utlont
        self.boktype = boktype
        self.fag_sjanger = fag_sjanger
                

        
        
# class Fagbok(Bok):
#     def __init__(self, titel:str, forfater:str, isbn:int, fag:str):
#         super().__init__(titel, forfater, isbn, "fagbok")
#         self.fag_sjanger = fag
        
# class literatur(Bok):
#     def __init__(self, titel:str, forfater:str, isbn:int, literaur:str):
#         super().__init__(titel, forfater, isbn, "literatur")
#         self.fag_sjanger = literaur
        
        