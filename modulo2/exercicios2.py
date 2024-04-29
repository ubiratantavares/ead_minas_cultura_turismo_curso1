from scipy.stats import norm

def calcular_z_score(confianca):
    # Convertendo o nível de confiança para a área sob a curva normal
    area = (1 + confianca) / 2
    # Calculando o Z-score correspondente à área
    z_score = norm.ppf(area)
    return z_score    # Calcula o percentil correspondente ao nível de confiança

def calcular_tamanho_amostra(popul, z_score, prop, me):
    """
    popul: tamanho da populacao
    prop: proporção de um resultado de uma característica importante do perfil da população
    z_score: escore da curva normal que é função do nível de confiança escolhido
    me: margem de erro
    n: tamanho da amostra
    """
    if (popul < 100_000):
        return round((z_score **2 * prop * (1 - prop) * popul) / (me **2 * (popul - 1) + z_score **2 * prop * (1 - prop)), 0)
    return round((z_score **2 * prop * (1 - prop)) / (me **2), 0)

def executar(dados):
    for valor in dados.values():
        z_score = calcular_z_score(valor[1])
        print(z_score)
        num_amostra = calcular_tamanho_amostra(valor[0], z_score, .5, valor[2])
        print(f"Tamanho da amostra: {num_amostra}")

def main():
    dados = {1: [5_500_000, .95, .05]}
    executar(dados)

if __name__ == "__main__":
    main()
