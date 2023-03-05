import lib
import action_csv

filename = "estado_media.csv"

def listar():
    lib.limpar_tela()
    lista = action_csv.ler(filename)
    for item in lista:
        print("-"*60)
        print("Estado: "+ item["Estado"])
        print("Média Salarial: " + item["Média Salarial"])
    input("Digite enter para continuar...")
    lib.limpar_tela()