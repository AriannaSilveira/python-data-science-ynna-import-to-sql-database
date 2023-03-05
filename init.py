import lib
import pais_populacao_estado
import estado_media
import merged_files

print("-" * 100)
print(" "* 40 + "SEJA BEM-VINDA, YNNA!")
print("-" * 100)

while(True):
    print("\nSelecione uma das opções abaixo:")
    print("1 - Ver informações dos paises e população com estado.")
    print("2 - Ver informações do estado com a média salarial da população.")
    print("3 - Ver informações das duas tabelas acima em conjunto.")
    print("4 - Importar essas informações(opção 3) para meu banco de dados.")
    print("5 - Sair.\n")

    op = int(input("Digite a opção: "))

    if op == 1:
        pais_populacao_estado.listar()
    elif op == 2:
        estado_media.listar()
    elif op == 3:
        merged_files.listar_merged()
    elif op == 4:
        merged_files.import_to_sql()
    elif op == 5:
        lib.limpar_tela()
        break
    else:
        lib.msg("Opção inválida!")