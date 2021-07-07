#Simulador de Dados
#Developed by: Lucas Gabriel

'''
Simulador de dados via shell do Windows.
'''


import random
import os
import time
import datetime

random.SystemRandom(datetime.datetime.now())

def sair():
    print("\n\nObrigado por jogar :-)")
    time.sleep(2)
    os.system("exit")
    
def simula_dado():
    valor = random.randint(1,6)
    print("\n\nNúmero da jogada: %i\n\n" % valor)

def main():
    print("--------------------------------------")
    print("         SIMULADOR DE DADO            ")
    print("--------------------------------------\n\n")

    
    print("Escolha uma opção logo abaixo....")
    print("---------------------------------")
    print("1.Jogar dado")
    print("2.Sair")

    
    
    try:
        opcao = int(input("\n\nDigite o número da opçao: "))
        if(opcao > 2 or opcao < 1):
            print("\n\nOpção Inválida!!!!")
            time.sleep(10)
            main()
            
        elif (opcao == 2):
            sair()
            
        else:
            simula_dado()
            while True:
                opcao = input("Deseja jogar o dado novamente [s/n]? ")

                if opcao.lower() == "s":
                    os.system("cls")
                    simula_dado()
                else:
                    sair()
                    break
                time.sleep(2)
    except KeyboardInterrupt:
        sair()
    except Exception as e:
        print("\n\nEntrada Inválida!!!!\n\n")
        print("Retornando ao menu!!!!")
        time.sleep(2)
        os.system("cls")
        main()

if __name__ == "__main__":
    main()
        
