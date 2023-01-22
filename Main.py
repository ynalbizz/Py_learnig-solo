import classes
from classes.Jogador import Jogador
from classes.npcs import Npc
def objTest(obj1,obj2):
    print("")
    print("")
    print(obj1)
    print("")
    print(obj2)
    print("")
    pass

pc = Jogador("Davi" , 100, 15,1)

npc = Npc("Npc", 30, 30,True,2)


objTest(pc,npc)


# print("hello")