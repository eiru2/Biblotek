from sys import path
path.append('../BIBLOTEK') 

import json
import funk.boker as bok
import funk.personer as Pr



biblo = bok.Biblotek("Jens biblotek", "skien")

a = bok.Bok("Harry poter", "jk rowling" , 1 , "literatur","fantasy" )
b = bok.Bok("Katt med støvler", "OLav" , 3 , "literatur", "fantasy" )
c = bok.Bok("Bio 2", "Jens" , 2 , "fagbok","Biologi" )


biblo.leggTilBok(a)
biblo.leggTilBok(b)
biblo.leggTilBok(c)

person = Pr.person("Er")

biblo.leggTilpersoner(person)

a.utlont = True

person.leggTilBok(a)

# for i in range(50):
#     c = bok.Bok(("Bio "+str(i)), "Jens" , i+4 , "fagbok" ,"Biologi" )
#     biblo.leggTilBok(c)

    # def save(self, path):
    #     f = open('data/maps/'+path, 'w')
    #     json.dump({'tilemap': self.tilemap , 'tile_size': self.tileSize,'offgrid': self.offgridTiile}, f)
    #     f.close()
    # # laster in map
    # def load(self,path):
    #     f = open('data/maps/'+path, 'r')
    #     map_data = json.load(f)
    #     f.close()
    #     self.tilemap = map_data['tilemap']
    #     self.tileSize = map_data['tile_size']
    #     self.offgridTiile = map_data['offgrid']


def oppstart(biblotek):
    """_summary_
        henter data og legger til i biblotk classen 
    Args:
        biblotek (class): biblotek calssen
    """
    try:
        f = open('Data/bok.json', 'r')
        map_data = json.load(f)
        f.close()
        for verdier in map_data.values() :
            biblotek.leggTilBok(bok.Bok(verdier["titel"], verdier["forfater"], verdier["isbn"],  verdier["boktype"], verdier["fag_sjanger"], verdier["utlont"],))
    except: print("fant ikke bok fil")
        
    try:
        f = open('Data/personer.json', 'r')
        map_data = json.load(f)
        f.close()
        for verdier in map_data.values():
            biblotek.leggTilpersoner(Pr.person(verdier["navn"]))
            for bokId in verdier["boker"]: # legger til bokid i boker listen
                biblotek.personer[-1].leggTilBok(bokId)
    except: print("fant ikke person fil")
    






def avslutt(biblotek):
    """_summary_
        Henter dataen å lagrer de i json format
    Args:
        biblotek (class): biblotek classen
    """
    biblotek.get_bokDict()
    print(biblotek.bokDict)
    biblotek.get_personDict()
    print(biblotek.boker)

    f = open('Data/bok.json', 'w')
    json.dump(biblotek.bokDict,f)
    f.close()
    
    f = open('Data/personer.json', 'w')
    json.dump(biblotek.personDict, f)
        
# print(biblo.personer)
# biblo.get_personDict()
# avslutt(biblo)
oppstart(biblo)
# print(biblo.personer[0].boker[0])


# print(biblo.bokDict)