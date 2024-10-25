import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

def obter_dados_ativos(simbolos, periodo='5y'):
    dados = yf.download(simbolos, period=periodo)['Adj Close']
    retornos_diarios = dados.pct_change().dropna()
    retorno_esperado = retornos_diarios.mean() * 252  # Retorno anualizado
    volatilidade = retornos_diarios.std() * np.sqrt(252)  # Risco anualizado
    matriz_covariancia = retornos_diarios.cov() * 252  # Covariância anualizada
    return retorno_esperado, volatilidade, matriz_covariancia

def otimizar_portfolio(retorno_esperado, matriz_covariancia, limite_risco):
    n = len(retorno_esperado)
    
    # Função objetivo: minimizar o retorno negativo para maximizar o retorno
    def funcao_objetivo(pesos):
        return -np.dot(pesos, retorno_esperado)
    
    # Restrição de risco (variância da carteira)
    def restricao_risco(pesos):
        return limite_risco - np.sqrt(np.dot(pesos.T, np.dot(matriz_covariancia, pesos)))
    
    # Restrição de soma dos pesos
    restricoes = ({'type': 'eq', 'fun': lambda pesos: np.sum(pesos) - 1},
                  {'type': 'ineq', 'fun': restricao_risco})
    
    # Limites para os pesos (0 a 1)
    limites = tuple((0, 1) for _ in range(n))
    
    # Pesos iniciais
    pesos_iniciais = np.ones(n) / n
    
    # Otimização
    resultado = minimize(funcao_objetivo, pesos_iniciais, method='SLSQP', bounds=limites, constraints=restricoes)
    
    return resultado.x  # Retorna os pesos otimizados
