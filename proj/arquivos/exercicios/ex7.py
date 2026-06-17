def calcular_medias_alunos():

    try:
        nomes_e_medias = [()]
        caminho_arquivo = 'proj/arquivos/exercicios/arquivos/notas.txt'
        with open(caminho_arquivo) as arquivo:
            for linha in arquivo.readlines():
                dados = linha.split(',')
                nome = dados[0], 
                nota1 = float(dados[1]) 
                nota2 = float(dados[2])
                media = (nota1 + nota2) / 2

                nomes_e_medias.append((nome, media))
    except FileNotFoundError:
        print('Arquivo não encontrado!!!')
    finally:
        if not nomes_e_medias:
            return None
        
        with open('medias_finais.txt', 'w') as arquivo:
            for objeto in nomes_e_medias:
                arquivo.write(f"{objeto}")

if __name__ == '__main__':
    calcular_medias_alunos()