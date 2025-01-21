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

def plotar_rota(melhor_rota, coordenadas, num_linhas):
    rota_completa = ['R'] + melhor_rota + ['R']
    x = [coordenadas[ponto][1] for ponto in rota_completa]
    y = [num_linhas - 1 - coordenadas[ponto][0] for ponto in rota_completa]
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Melhor Rota')
    for i in range(len(x) - 1):
        plt.annotate("", xy=(x[i + 1], y[i + 1]), xytext=(x[i], y[i]),
                     arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
    for ponto, (i, j) in coordenadas.items():
        plt.text(j, num_linhas - 1 - i, ponto, fontsize=12, ha='right', color="blue")
    plt.title("Melhor Rota Encontrada")
    plt.grid(True)
    plt.legend()
    plt.xlim(0, max(x) + 1)
    plt.ylim(0, max(y) + 1)
    plt.xticks(range(0, max(x) + 2))
    plt.yticks(range(0, max(y) + 2))
    plt.show()

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
    plotar_rota(melhor_rota, coordenadas, len(matriz))

if __name__ == "__main__":
    principal()
