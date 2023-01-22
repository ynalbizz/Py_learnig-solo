
from classes.PersonagemModulo import Personagem


class Jogador(Personagem):

    


   

    def ataqueEspecial(this, alvo):
        alvo.perderVida(this.dano*2)
    

    pass