import csv
import random
import os


# Caminho para o diretório onde o script está localizado
caminho_do_script = os.path.dirname(os.path.abspath(__file__))

# Caminho para o diretório "data"
diretorio_data = os.path.join(caminho_do_script, "data")
arquivo_csv = os.path.join(diretorio_data, "resultados_d20.csv")

# Garante que o diretório "data" exista
if not os.path.exists(diretorio_data):
    os.makedirs(diretorio_data)


def rolar_d20():
    return random.randint(1, 20)

# Lista para armazenar os resultados
resultados = []

for i in range(1, 101):
    random.seed(os.urandom(8))  # Semente baseada em bytes aleatórios
    rolagem = rolar_d20()
    if rolagem == 20:
        status = "Crítico"
    elif rolagem == 1:
        status = "Falha Crítica"
    else:
        status = "Normal"
    resultados.append((i, rolagem, status))

# Salvando os resultados 
with open(arquivo_csv, mode="w", newline="") as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(["Rolagem", "Resultado", "Status"])  
    escritor_csv.writerows(resultados)

print(f"Resultados salvos em {arquivo_csv}")
