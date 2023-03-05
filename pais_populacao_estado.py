import lib
import action_csv

filename = "pais_populacao_estado.csv"

def listar():
    lib.limpar_tela()
    lista = action_csv.ler(filename)
    for item in lista:
        print("-"*60)
        print("País: "+ item["País"])
        print("Estado: " + item["Estado"])
        print("População: " + item["População"])
    input("Digite enter para continuar...")
    lib.limpar_tela()