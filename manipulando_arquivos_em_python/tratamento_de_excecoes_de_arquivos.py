from pathlib import Path

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError as exc:
    print("O arquivo não foi encontrado.")
    print(exc)
    
ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / 'arquivo_inexistente.txt', 'r')
except IsADirectoryError as exc:
    print("Você tentou abrir um diretório ao invés de um arquivo.")
    print(exc)
except IOError as exc:
    print("Ocorreu um erro ao abrir o arquivo.")
    print(exc)
except Exception as exc:
    print("Ocorreu um erro inesperado.")
    print(exc)