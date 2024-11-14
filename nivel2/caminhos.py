# absoluto= "C:\Users\Rafael\Documents\Projetos\programacao_dinamica_python\caminhos.py"
# relativo = "nivel2\caminhos.py"

import os

# DATA_DIR = 'nivel2'
# print(os.path.abspath(DATA_DIR))

# caminho = os.path.join(os.path.abspath(DATA_DIR), 'caminhos.py')
# print(caminho)

# print(os.listdir("C:\\Users\\Rafael\\Documents\\Projetos\\"))

# modulos_python = []
# for nome in os.listdir(DATA_DIR):
#   if nome.endswith(".py"):
#     modulos_python.append(nome)
  
# print(modulos_python)


OUTPUT_DIR = "saidas"
nome_arquivo = "mensagem.txt"

if not os.path.exists(OUTPUT_DIR):
  os.makedirs(OUTPUT_DIR)


with open(os.path.join(OUTPUT_DIR, nome_arquivo), 'w') as arq:
  arq.write("Teste Rafael")

