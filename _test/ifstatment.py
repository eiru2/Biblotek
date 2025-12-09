class Forfater:
    def __init__(self, navn:str):
        self.navn = navn
        self.boker = []

forfater = []

run = True


while run:
    x = input()
    if x == "exit":
        run = False
        break
    if x not in forfater.navn:
        forfater.append(Forfater(x))
    print(forfater)
    