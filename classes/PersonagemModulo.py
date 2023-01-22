

racas = ["Humano","Elfo","Anão"]

class Personagem:
    
    

    def __init__(this, name, vida, dano, raca):
        this.nome = name
        this.vida = vida
        this.dano = dano
        this.estado = "Vivo"
        this.setRaca(raca)


    def setRaca(this, raca):
        this.raca = racas[raca-1]



    def __str__(self):

        mensagem = f"Nome: {self.nome} // Vida:  {self.vida} // Estado:  {self.estado} // Raça: {self.raca}"
        return f"{mensagem}" 
    

    def atacar(this, alvo):
        alvo.perderVida(this.dano)

        pass

    def perderVida(this,dano):

        vida = this.vida - dano
        if vida <= 0:
            vida = 0
            this.estado = "morto"
        this.vida = vida
        pass
