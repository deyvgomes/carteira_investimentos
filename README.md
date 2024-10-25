# Otimização de Carteira de Investimentos com Risco Limitado

# Objetivo do Projeto
Este projeto é uma implementação de um algoritmo de otimização de carteira de investimentos, baseado no problema da mochila, que visa maximizar o retorno esperado de uma carteira de ativos financeiros respeitando um limite de risco aceitável. A abordagem envolve o uso de modelos de medição de risco, como volatilidade, e integra coleta de dados via API do Yahoo Finanças para análise dos ativos financeiros.

# Metodologia

A otimização da carteira é baseada na seguinte abordagem:

# Modelagem Matemática: 
Adaptamos o problema da mochila, onde os ativos financeiros (itens) têm retorno esperado (valor) e risco (peso). O objetivo é maximizar o retorno total da carteira respeitando a "capacidade da mochila", que representa o limite de risco permitido.

# Implementação de Algoritmo:
Dados de Ativos: Coletamos dados dos ativos financeiros usando a biblioteca yfinance.
Cálculo do Risco e Retorno: Anualizamos o retorno esperado e a volatilidade (como medição de risco).
Otimização: Usamos a biblioteca scipy.optimize para encontrar a alocação ótima de ativos na carteira.

# Visualização dos Resultados:

Fronteira Eficiente: 
Mostra o equilíbrio entre retorno esperado e risco.

Distribuição de Ativos: Exibe a alocação de ativos em gráfico de pizza.

Evolução de Retorno e Risco: Representa graficamente o desempenho e o risco ao longo do tempo.


# Tecnologias Utilizadas

Linguagem: Python

Bibliotecas:
numpy e pandas: Manipulação de dados
scipy.optimize: Função de otimização
yfinance: Coleta de dados financeiros
matplotlib e seaborn: Visualização dos dados e gráficos


# Pré-requisitos e Instalação
1. Clonar o Repositório

git clone https://github.com/devgomes/otimizacao_carteira.git
cd otimizacao_carteira

2. Instalar as Dependências 
Certifique-se de ter o Python instalado. Instale as dependências com o seguinte comando:
pip install -r requirements.txt

O arquivo requirements.txt deve incluir:
plaintext
Copiar código
numpy
pandas
yfinance
scipy
matplotlib
seaborn


# Execução do Projeto

1. Definir Parâmetros de Entrada

No arquivo principal (otimizacao_carteira.py), defina os ativos a serem analisados e o limite de risco da carteira, conforme exemplo:

simbolos = ['AAPL', 'GOOGL', 'AMZN']
limite_risco = 0.20


2. Executar o Algoritmo

Execute o código para calcular os pesos otimizados da carteira:
python otimizacao_carteira.py


3. Visualizar Resultados

O script gera gráficos para visualização da carteira, incluindo a Fronteira Eficiente, Alocação de Ativos e Evolução do Retorno e Risco.


# Exemplo de Resultados e Visualizações

1. Fronteira Eficiente
Este gráfico exibe o retorno esperado em relação ao risco da carteira, mostrando o ponto de equilíbrio ideal entre retorno e volatilidade.

2. Alocação de Ativos
Um gráfico de pizza apresenta a distribuição de ativos na carteira otimizada.

3. Histórico de Desempenho
Um gráfico de linha mostra a evolução do retorno e do risco ao longo do tempo, ajudando na análise de desempenho.



# Estrutura do Projeto

main.py: Executa o fluxo principal do projeto, chamando as funções de coleta de dados, otimização de portfólio e visualização dos resultados.

otimizacao.py: Contém a lógica para otimizar a alocação dos ativos com base no retorno e no risco esperado.

visualizacao.py: Responsável pela geração dos gráficos, incluindo a alocação de ativos e a fronteira eficiente.

README.md: Arquivo de documentação explicando o objetivo, abordagem e instruções de uso.

requirements.txt: Lista de dependências para instalação.


# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um "issue" ou enviar um "pull request" com sugestões, correções de bugs ou melhorias.