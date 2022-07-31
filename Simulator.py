#Simulador de dado em python

import random

class simulador_dado:
    def __init__(self):
        self.valor_inicial = 1
        self.valor_final = 6
    
    def iniciar(self):
        while True:
            pergunta = input("Voçê gostaria de girar o dado? ")
            if pergunta == "sim":
                print(random.randint(self.valor_inicial,self.valor_final))
            elif pergunta == "nao":
                print("Obrigado!")
                break
            else:
                print("digite novamente.")

simulador_de_dados = simulador_dado()
simulador_de_dados.iniciar()
