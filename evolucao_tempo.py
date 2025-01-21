import time
import matplotlib.pyplot as plt

def permutacoes(lista):
    if len(lista) == 1:
        return [lista]
    lista_auxiliar = []
    for i, elemento_atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i+1:]
        for perm in permutacoes(elementos_restantes):
            lista_auxiliar.append([elemento_atual] + perm)
    return lista_auxiliar

def calcular_distancia(rota, coordenadas):
    custo_total = 0
    rota_completa = ['R'] + rota + ['R']
    for i in range(len(rota_completa) - 1):
        ponto1 = coordenadas[rota_completa[i]]
        ponto2 = coordenadas[rota_completa[i + 1]]
        custo_total += abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])
    return custo_total

# 3 pontos de entrega
t1 = time.time()
def principal():
    matriz = [
        ['0', 'A', '0', '0', '0'],
        ['0', '0', '0', '0', 'C'],
        ['R', '0', 'B', '0', '0']
    ]
    coordenadas = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor != '0':
                coordenadas[valor] = (i, j)
    pontos = [ponto for ponto in coordenadas.keys() if ponto != 'R']
    lista_permutacoes = permutacoes(pontos)
    menor_custo = float('inf')
    melhor_rota = None
    for perm in lista_permutacoes:
        custo = calcular_distancia(perm, coordenadas)
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm
    print("\nMelhor rota encontrada:")
    print(f"Rota: {' -> '.join(melhor_rota)}, Custo: {menor_custo}")

if __name__ == "__main__":
    principal()
t2 = time.time()
tempo_3 = t2 - t1

# 4 pontos de entrega
t1 = time.time()
def principal():
    matriz = [
        ['0', '0', '0', '0', 'D'],
        ['0', 'A', '0', '0', '0'],
        ['0', '0', '0', '0', 'C'],
        ['R', '0', 'B', '0', '0']
    ]
    coordenadas = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor != '0':
                coordenadas[valor] = (i, j)
    pontos = [ponto for ponto in coordenadas.keys() if ponto != 'R']
    lista_permutacoes = permutacoes(pontos)
    menor_custo = float('inf')
    melhor_rota = None
    for perm in lista_permutacoes:
        custo = calcular_distancia(perm, coordenadas)
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm
    print("\nMelhor rota encontrada:")
    print(f"Rota: {' -> '.join(melhor_rota)}, Custo: {menor_custo}")

if __name__ == "__main__":
    principal()
t2 = time.time()
tempo_4 = t2 - t1

# 5 pontos de entrega
t1 = time.time()
def principal():
    matriz = [
        ['0', '0', '0', '0', 'D', '0'],
        ['0', 'A', '0', '0', '0', '0'],
        ['0', '0', '0', '0', 'C', '0'],
        ['R', '0', 'B', '0', '0', 'E']
    ]
    coordenadas = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor != '0':
                coordenadas[valor] = (i, j)
    pontos = [ponto for ponto in coordenadas.keys() if ponto != 'R']
    lista_permutacoes = permutacoes(pontos)
    menor_custo = float('inf')
    melhor_rota = None
    for perm in lista_permutacoes:
        custo = calcular_distancia(perm, coordenadas)
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm
    print("\nMelhor rota encontrada:")
    print(f"Rota: {' -> '.join(melhor_rota)}, Custo: {menor_custo}")

if __name__ == "__main__":
    principal()
t2 = time.time()
tempo_5 = t2 - t1

# 6 pontos de entrega
t1 = time.time()
def principal():
    matriz = [
        ['F', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', 'D', '0'],
        ['0', 'A', '0', '0', '0', '0'],
        ['0', '0', '0', '0', 'C', '0'],
        ['R', '0', 'B', '0', '0', 'E']
    ]
    coordenadas = {}
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor != '0':
                coordenadas[valor] = (i, j)
    pontos = [ponto for ponto in coordenadas.keys() if ponto != 'R']
    lista_permutacoes = permutacoes(pontos)
    menor_custo = float('inf')
    melhor_rota = None
    for perm in lista_permutacoes:
        custo = calcular_distancia(perm, coordenadas)
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm
    print("\nMelhor rota encontrada:")
    print(f"Rota: {' -> '.join(melhor_rota)}, Custo: {menor_custo}")

if __name__ == "__main__":
    principal()
t2 = time.time()
tempo_6 = t2-t1

# Criação do gráfico
tempos = [tempo_3, tempo_4, tempo_5, tempo_6]
pontos = ['3 Pontos', '4 Pontos', '5 Pontos', '6 Pontos']

plt.plot(pontos, tempos, marker='o', linestyle='-', color='b')

plt.title("Evolução do Tempo")
plt.xlabel("Entregas")
plt.ylabel("Tempo (segundos)")

plt.show()
