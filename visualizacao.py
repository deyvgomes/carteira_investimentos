import pandas as pd
import matplotlib.pyplot as plt

# Definindo cores específicas para cada ativo
cores_ativos = {
    'AAPL': 'blue',
    'GOOGL': 'green',
    'AMZN': 'orange'
}

def visualizacao_portfolio(pesos, retorno_esperado, volatilidade):
    ativos = retorno_esperado.index
    alocacao = pd.Series(pesos, index=ativos)
    
    # Gráfico de Alocação de Ativos com cores específicas
    plt.figure(figsize=(10, 6))
    alocacao.plot(kind='pie', autopct='%1.1f%%', colors=[cores_ativos[ativo] for ativo in ativos])
    plt.title('Alocação de Ativos na Carteira Otimizada')
    plt.show()

    # Gráfico da Fronteira Eficiente com cores específicas para cada ativo
    plt.figure(figsize=(10, 6))
    for ativo in ativos:
        plt.scatter(volatilidade[ativo], retorno_esperado[ativo], color=cores_ativos[ativo], label=ativo)
    plt.xlabel('Risco (Volatilidade)')
    plt.ylabel('Retorno Esperado')
    plt.title('Fronteira Eficiente')
    plt.legend()
    plt.show()
