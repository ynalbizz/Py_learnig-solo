from classes.PersonagemModulo import Personagem
class Npc(Personagem):
    # conduta = any
    # racaId = None
    
    def __init__(this, name, vida, dano, inimigo, raca):
        
        this.nome = name
        this.vida = vida
        this.dano = dano
        if inimigo == True:
            this.conduta = "Agressiva"
        elif inimigo == False:
            this.conduta = "Passiva"
        else:
            this.conduta = "Neutra"
        this.raca = this.setRaca(raca)
        this.estado = "Vivo"
        


    def __str__(self):

        mensagem = f"Nome: {self.nome} // Vida:  {self.vida} // Estado:  {self.estado} //Conduta: {self.conduta} // Raça: {self.raca}"
        return f"{mensagem}" 
       


    def setRaca(this, racaId):
        if this.conduta == "Agressiva":
            if racaId == 1:
               return "Humano"
            elif racaId == 2:
                return "Dragão"
            elif racaId == 3:
                return "Orc"
            elif racaId == 4:
                return "Animal Selvagem"
            elif racaId == 5:
                return "Espirito elemental"
            elif racaId == 6:
                return "Demonio"
        else:
            if racaId == 1:
                return "Humano"
            elif racaId == 2:
                return  "Elfo"
            elif racaId == 3:
                return "Anão"
            elif racaId == 4:
                return "Dragão"
            elif racaId == 5:
                return "Fada"
            elif racaId == 6:
                return "Espirito elemental"



pass