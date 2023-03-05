import pandas as pd
import pyodbc
import lib

def listar_merged():
    lib.limpar_tela()
    pais_populacao_estado_df = pd.read_csv("pais_populacao_estado.csv")
    estado_media_df = pd.read_csv("estado_media.csv")

    merged_df = pd.merge(pais_populacao_estado_df, estado_media_df, on='Estado')
    
    print(merged_df)
    input("Digite enter para continuar...")
    lib.limpar_tela()
    return merged_df

def import_to_sql():
    lib.limpar_tela()
    print("Ynna, vamos importar os seguintes dados em seu banco de dados:")
    merged_df = listar_merged()
    
    conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:data-lake-ynna.database.windows.net,1433;Database=exercicio_ynna;Uid=administrador;Pwd=N3po3001;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    print("Conexão com banco de dados estabelecida...")
    input("Digite enter para continuar...")

    conn.execute("DROP TABLE IF EXISTS Pais_Populacao_Estado_Media")
    conn.execute("CREATE TABLE Pais_Populacao_Estado_Media (Pais varchar(255), Estado varchar(255), Populacao int, MediaSalarial float)")
    print("Tabela criada em seu banco de dados...")

    for index, row in merged_df.iterrows():
        conn.execute("INSERT INTO Pais_Populacao_Estado_Media (Pais, Estado, Populacao, MediaSalarial) VALUES(?, ?, ?, ?)", row[0], row[1], row[2], row[3])
    
    print("Informações inseridas...")
    input("Digite enter para continuar...")

    conn.commit()
    print("Importação executada!")
    input("Digite enter para continuar...")

    conn.close()
    print("Conexão com banco de dados finalizada.")
    input("Digite enter para continuar...")
    lib.limpar_tela()