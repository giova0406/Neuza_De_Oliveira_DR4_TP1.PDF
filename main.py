
#  Exercício 1 Atualizar dicionário de estoque de livros
estoque = {
    "Python Crash Course": 4,
    "Clean Code": 2,
    "Automate the Boring Stuff": 0
}

def atualizar_estoque(estoque, livro, quantidade):
    if livro in estoque:
        estoque[livro] += quantidade
    else:
        estoque[livro] = quantidade
    if estoque[livro] == 0:
        del estoque[livro]
    print(estoque)
    return estoque
atualizar_estoque(estoque, "Clean Code", 3)
atualizar_estoque(estoque, "Fluent Python", 5)
atualizar_estoque(estoque, "Automate the Boring Stuff", 0)

# Exercício 2 Criar dicionário de notas por aluno

registros = [
    ("Ana", [8, 9, 7]),
    ("Bruno", [5, 6, 5]),
    ("Carla", [10, 9, 10])
]
notas = {}

for aluno, lista in registros:
    notas[aluno] = lista

notas["Daniel"] = [7, 7, 8]
remover = []

for aluno, lista in notas.items():
    media = sum(lista) / len(lista)
    if media < 6:
        remover.append(aluno)

for aluno in remover:
    del notas[aluno]

print(notas)

# Exercício 3 Comparar desempenho de buscas em lista e dicionário

import time

sensores_lista = [("S1", 34), ("S2", 36), ("S3", 37), ("S4", 38)]
sensores_dict = {"S1": 34, "S2": 36, "S3": 37, "S4": 38}

tempos_lista = []
tempos_dict = []

for i in range(10000):
    # busca na lista
    inicio = time.time()
    for chave, valor in sensores_lista:
        if chave == "S3":
            resultado = valor
    fim = time.time()
    tempos_lista.append(fim - inicio)

    # busca no dicionário
    inicio = time.time()
    resultado = sensores_dict["S3"]
    fim = time.time()
    tempos_dict.append(fim - inicio)

media_lista = sum(tempos_lista) / len(tempos_lista)
media_dict = sum(tempos_dict) / len(tempos_dict)

print(f"Tempo medio (lista): {media_lista:.6f} segundos")
print(f"Tempo medio (dict): {media_dict:.6f} segundos")

# Exercício 4 Converter dicionário em lista tabular
medias = {"Ana": 8.5, "Bruno": 6.3, "Carla": 9.1}

tabela = list(medias.items())

ranking = sorted(tabela, key=lambda item: item[1], reverse=True)
print(ranking)

# Exercício 5 Remover leituras incorretas
temperaturas = {"RJ": 29.4, "SP": -99.0, "MG": 27.2, "BA": 31.1, "RS": -88.0}

def filtrar_temperaturas(temp_dict):
    novo = {}

    for estado, temp in temp_dict.items():
        if temp >= -50:
          novo[estado] = temp
    removido = len(temp_dict) - len(novo)
    print("Removidos:", removido)
    print("Restantes:", len(novo))
    return novo

filtrar_temperaturas(temperaturas)

# Exercício 6 Atualizar estoque com vencimento
import datetime

medicamentos = {
    "Aspirina": "2024-11-01",
    "Dipirona": "2026-03-10",
    "Paracetamol": "2023-12-01"
}

hoje = datetime.date.today()
remover = []

for nome, validade in medicamentos.items():
    data = datetime.datetime.strptime(validade, "%Y-%m-%d").date()
    if data < hoje:
        remover.append(nome)

for med in remover:
    del medicamentos[med]

print("Removidos:", len(remover))
print(medicamentos)

# Exercício 7 Garantir unicidade

emails = [
    "ana@empresa.com", "bruno@empresa.com", "ana@empresa.com",
    "carla@empresa.com", "bruno@empresa.com", "daniel@empresa.com"
]

unicos = set(emails)
duplicatas = len(emails) - len(unicos)
lista_final = sorted(unicos)

print("Duplicatas removidas:", duplicatas)
print(lista_final)

# Exercício 8 Analisar interseção e diferença entre conjuntos

clientes_A = {"Ana", "Bruno", "Carla", "Daniel"}
clientes_B = {"Bruno", "Carla", "Eduardo", "Fernanda"}

intersecao = clientes_A & clientes_B
so_em_A = clientes_A - clientes_B
uniao = clientes_A | clientes_B

print("Clientes em comum:", intersecao)
print("So em A:", so_em_A)
print("Todos os clientes:", uniao)

print("Total Unico:", len(uniao))

# Exercício 9 Ler arquivo e contar palavras

with open("relatorio.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    
import string

contagem = {}

for linha in linhas:
    for palavra in linha.split():
        palavra = palavra.strip(string.punctuation).lower()
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
top3 = ranking[:3]

print("Top 3 palavras mais frequentes:")
for palavra, qnt in top3:
    print(f"{palavra}: {qnt}")

# Exercício 10 Gerar arquivo de configuração
config = {
    "servidor": "192.168.0.10",
    "porta": 8080,
    "modo": "produção"
}
#open("config.txt", "w") → abre para escrever
with open("config.txt", "w", encoding="utf-8") as arquivo: 
    arquivo.write("texto aqui\n")

#write(f"{chave}: {valor}\n") → grava cada par
with open("config.txt", "w", encoding="utf-8") as arquivo:
    for chave, valor in config.items():
        arquivo.write(f"{chave}: {valor}\n")

#open("config.txt", "r") → abre para ler
with open("config.txt", "r", encoding="utf-8") as arquivo:
    conteudo= arquivo.read()
    print(conteudo)

# Exercício 11 Converter dicionário em JSON
import json

produtos = {
    "Smartphone": {"preco": 2500, "estoque": 12},
    "Notebook": {"preco": 4800, "estoque": 5},
    "Fone Bluetooth": {"preco": 300, "estoque": 25}
}

with open("produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    
with open("produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(type(dados))
print(dados)

# Exercício 12 Consolidar bases e exportar para JSON
campanha_1 = ["Ana", "Bruno", "Carla"]
campanha_2 = ["Bruno", "Daniel", "Eduardo"]
campanha_3 = ["Ana", "Fernanda", "Gustavo"]

set1 = set(campanha_1)
set2 = set(campanha_2)
set3 = set(campanha_3)

base_unica = set1 | set2 | set3
dados = {
    "total": len(base_unica),
    "nomes": list(base_unica)
}
with open("clientes_unicos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

with open("clientes_unicos.json", "r", encoding="utf-8") as arquivo:
    resultado = json.load(arquivo)
    print("Total de clientes:", resultado["total"])