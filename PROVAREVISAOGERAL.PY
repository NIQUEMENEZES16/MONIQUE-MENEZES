import os

# Pega o caminho do diretório atual
diretorio = os.getcwd()

# Lista todos os itens no diretório
itens = os.listdir(diretorio)

# Listas para arquivos e pastas
arquivos = []
pastas = []

# Verifica cada item e separa em arquivo ou pasta
for item in itens:
    caminho = os.path.join(diretorio, item)
    if os.path.isfile(caminho):
        arquivos.append(item)
    elif os.path.isdir(caminho):
        pastas.append(item)

# Mostra as pastas
print("Pastas:")
for p in pastas:
    print(p)

# Mostra os arquivos
print("\nArquivos:")
for a in arquivos:
    print(a)
