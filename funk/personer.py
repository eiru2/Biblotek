class person:
    def __init__(self, navn:str):
        """_summary_

        Args:
            navn (str): navn po person som låner en bok
        """
        self.navn = navn
        self.boker = []
    
    def leggTilBok(self,bok):
        self.boker.append(bok)
        
class forfater(person):
    def __init__(self, navn:str):
        """_summary_

        Args:
            navn (str): navn po forfater som låner en bok
        """
        super().__init__(navn)