import csv
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

try:
    with open(ROOT_PATH / "dados.csv", "w", encoding='utf-8', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        escritor.writerow(['Alice', 30, 'São Paulo'])
        escritor.writerow(['Bob', 25, 'Rio de Janeiro'])
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")

# try:
#     with open(ROOT_PATH / "dados.csv", "r", encoding='utf-8') as file:
#         leitor = csv.reader(file)
#         for linha in leitor:
#             print(linha)

# except IOError as e:
#     print(f"Erro ao escrever no arquivo: {e}")

try:
    with open(ROOT_PATH / "dados.csv", "r", encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            print(f"{linha['Nome']} tem {linha['Idade']} anos e mora em {linha['Cidade']}")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")