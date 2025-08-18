from pathlib import Path
"""
Este script lê e imprime o conteúdo de um arquivo de texto chamado 'Lorem lipsum.txt' localizado no mesmo diretório do arquivo Python.
Boas práticas adotadas:
- Utilização do módulo `pathlib` para manipulação de caminhos de arquivos de forma mais robusta e multiplataforma.
- Uso do contexto `with open(...)` para garantir que o arquivo seja fechado automaticamente após o uso, evitando vazamentos de recursos e possíveis erros.
- Definição da constante `ROOT_PATH` baseada no caminho do arquivo atual (`__file__`), tornando o código mais portável e fácil de manter.
Essas práticas aumentam a legibilidade, segurança e portabilidade do código.
"""

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / 'Lorem lipsum.txt') as arquivo:
    # Lê o conteúdo do arquivo
    conteudo = arquivo.read()
    print(conteudo)


try:
    with open(ROOT_PATH / 'arquivo_inexistente.txt') as arquivo:
        conteudo = arquivo.read()
except IOError as exc:
    print("Ocorreu um erro ao abrir o arquivo.")
    print(exc)
    
    
try:
    with open(ROOT_PATH / 'Lorem lipsum.txt', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except IOError as exc:
    print("Ocorreu um erro ao abrir o arquivo encoding.")
    print(exc)