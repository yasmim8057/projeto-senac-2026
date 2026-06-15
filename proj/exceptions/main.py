from casa import Casa
from chave import Chave
from minha_excecao import ChaveErradaError

if __name__ == '__main__':

    chave = Chave()
    casa = Casa(1234, chave)

    try:
        casa.abrir_porta(chave)
    except ChaveErradaError:
        
        chave.troca_codigo(1234)
        casa.troca_chave(chave)
        print(casa.abrir_porta(chave))
    

        

        
    
