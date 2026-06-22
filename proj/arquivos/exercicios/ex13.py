def gerar_planta_de_csv(nome_arquivo_csv: __file__, nome_arquivo_txt):

    planta = []
    try:
        with open(nome_arquivo_csv) as csv:
            for line in csv.readlines():
                if line.find('Parede'):
                    line.split(',')
                    
