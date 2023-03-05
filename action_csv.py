import csv

def ler(filename):
    dados = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append(dict(row))
    return dados