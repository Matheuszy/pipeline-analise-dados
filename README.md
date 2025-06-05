# 📊 Análise de Cancelamento de Clientes

Este projeto realiza uma análise exploratória de dados de cancelamento de clientes utilizando Python, com as bibliotecas **Pandas** e **Plotly**. O objetivo é identificar padrões, entender os principais motivos de churn e gerar visualizações interativas para facilitar a tomada de decisão.

## 🔧 Tecnologias utilizadas

- Python 3.x
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- Jupyter Notebook (opcional, mas recomendado)

## 📁 Estrutura do Projeto

.
├── dados/
│ └── cancelamentos.csv # Base de dados com informações de clientes cancelados
├── src/
│ └── analise_cancelamento.py # Script principal com análise e gráficos
├── README.md
└── requirements.txt # Dependências do projeto


## 📈 O que a análise inclui?

- Limpeza e tratamento de dados
- Análise de distribuição por:
  - Gênero
  - Idade
  - Tempo de contrato
  - Tipo de serviço
- Cálculo da taxa de churn
- Gráficos interativos com Plotly

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/matheuszy/pipeline-analise-dados.git
   cd pipeline-analise-dados

2. Instale as dependências:


Copiar
Editar
pip install -r requirements.txt
Execute o script:


Copiar
Editar
python src/analise_cancelamento.py
Ou abra o notebook, se houver:


Copiar
Editar
jupyter notebook

📌 Requisitos
Python 3.8+

Pandas

Plotly

Você pode instalar tudo com:


pip install pandas plotly