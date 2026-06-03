# Exercício 1
frutas = ['maçã', 'banana', 'laranja', 'morango']

def primeira_fruta(frutas: list):
    return frutas[0]

# Exercício 2
animais = ['gato', 'cachorro', 'passarinho', 'coelho']

def ultimo_animal(animais: list):
    return animais[-1]

#Exercício 3:
compras = []

def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')

    return compras

# Exercício 4
notas = [7.5, 8.0, 6.0, 9.5, 10.0]
def quantidade_notas(notas: list):
    return len(notas)

#Exercício 5
cores = ['vermelho', 'verde', 'azul']

def mudar_cor(cores: list):
    indice = cores.index('verde')
    cores[indice] = 'amarelo'
    return cores

#Exercício 6
tarefas = ['estudar', 'limpar quarto', 'lavar louça']
def esvaziar_tarefas(tarefas: list):
    tarefas.clear()
    return tarefas

#Exercício 7
respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']
def contar_sim(respostas: list):
    return respostas.count('Sim')

#Exercício 8
fila = ['Ana', 'Bruno', 'Carlos', 'Diego']
def remover_ultimo(fila: list):
    return fila.pop()

#Exercício 9
canais = ['Globo', 'SBT', 'Record', 'Band']

def posicao_sbt(canais: list):
    return canais.index('SBT')

# Exercício 10
dias = ['Segunda', 'Quarta', 'Quinta']
def ajustar_terca(dias: list):
    dias.insert(1, 'Terça')
    return dias

if __name__ == '__main__':
    print("Resultado exercício 1: ")
    fruta = primeira_fruta(frutas)
    print(fruta)

    print("\n Resultado exercício 2:")
    animal = ultimo_animal(animais)
    print(animal)

    print("\n Resultado exercício 3:")
    lista_compras = adicionar_compras(compras)
    print(lista_compras)

    print("\n Resultado exercício 4:")
    print(quantidade_notas(notas))

    print("\n Resultado exercício 5:")
    lista_cores = mudar_cor(cores)
    print(lista_cores)

    print("\n Resultado exercício 6:")
    lista_tarefas_vazia = esvaziar_tarefas(tarefas)
    print(lista_tarefas_vazia)

    print("\n Resultado exercício 7:")
    contagem_sim = contar_sim(respostas)
    print(contagem_sim)

    print("\n Resultado exercício 8:")
    pessoa_removida = remover_ultimo(fila)
    print(pessoa_removida)

    print("\n Resultado exercício 9:")
    indice_sbt = posicao_sbt(canais)
    print(indice_sbt)

    print("\n Resultado exercício 10:")
    semana = ajustar_terca(dias)
    print(semana)