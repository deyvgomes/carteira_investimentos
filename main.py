from otimizacao import obter_dados_ativos, otimizar_portfolio
from visualizacao import visualizacao_portfolio

# Definindo os símbolos dos ativos e o limite de risco
simbolos = ['AAPL', 'GOOGL', 'AMZN']  # Ativos de exemplo
limite_risco = 0.20  # Ajuste este valor para o risco tolerável

# Coleta de dados e cálculo do retorno e risco
retorno_esperado, volatilidade, matriz_covariancia = obter_dados_ativos(simbolos)

# Otimização da carteira
pesos_otimizados = otimizar_portfolio(retorno_esperado, matriz_covariancia, limite_risco)

# Visualização dos resultados
visualizacao_portfolio(pesos_otimizados, retorno_esperado, volatilidade)
