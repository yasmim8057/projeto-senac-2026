class Conversor:

    def converter_para_inteiro(self, texto:str) -> int:
        try:
            numero = int(texto)
        except ValueError:
            return 'Conversão inválida'
        
        return numero