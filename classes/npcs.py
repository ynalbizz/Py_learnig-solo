from classes.PersonagemModulo import Personagem

global racasNãoAgressivas
global racasAgressivas
racasAgressivas = ["Humano","Dragão","Orc","Animal Selvagem","Espirito Elemental","Demonio"]
racasNãoAgressivas = ["Humano","Dragão","Anão","Elfo","Espirito Elemental","Fada"]
    

class Npc(Personagem):
    
    def __init__(this, name, vida, dano, inimigo, raca):
        
        this.nome = name
        this.vida = vida
        this.dano = dano
        this.conduta = this.setConduta(inimigo)
        this.raca = this.setRaca(raca)
        this.estado = "Vivo"
        
    

    def __str__(self):

        mensagem = f"Nome: {self.nome} // Vida:  {self.vida} // Estado:  {self.estado} //Conduta: {self.conduta} // Raça: {self.raca}"
        return f"{mensagem}" 
       


    def setConduta(this,inimigo):
        if inimigo == True:
            return  "Agressiva"
        elif inimigo == False:
            return "Passiva"
        else:
            return "Neutra"
        


    def setRaca(this, racaId):
        if this.conduta == "Agressiva":
            return racasAgressivas[racaId-1]
        else:
            return racasNãoAgressivas[racaId-1]



pass