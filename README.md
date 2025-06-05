# Análise de Cancelamento de Serviço Bancário

Este projeto tem como objetivo principal **analisar os fatores que levam clientes a cancelar um serviço bancário**, fornecendo insights valiosos para a tomada de decisões estratégicas e a implementação de ações preventivas.

---

## 📊 Visão Geral do Projeto

A pipeline de análise de dados desenvolvida aqui processa informações de cancelamento, identifica padrões e sugere soluções baseadas nos dados. Utilizamos Python com as bibliotecas Pandas para manipulação de dados e Plotly Express para visualizações interativas.

---

## 📁 Estrutura do Projeto

etl-analise-dados/
├── .venv/                         # Ambiente virtual Python
├── dados/
│   └── cancelamentos.csv          # Conjunto de dados brutos de cancelamentos
├── src/
│   ├── analise.py                 # Script principal da pipeline de análise (código refatorado)
│   └── analise_cancelamentos.ipynb # Notebook Jupyter com o mesmo código para exploração interativa
├── .gitignore                     # Arquivo para ignorar arquivos e pastas no controle de versão (Git)
├── anotacoes.txt                  # Análises detalhadas e insights extraídos dos dados
├── README.md                      # Este arquivo de documentação
└── requirements.txt               # Dependências do projeto

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a pipeline de análise:

1.  **Clone o Repositório (se estiver em Git):**
    ```bash
    git clone git@github.com:Matheuszy/pipeline-analise-dados.git
    cd pipeline-analise-dados
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    source .venv/bin/activate
    ```
3.  **Instale as Dependências:**
    Com o ambiente virtual ativado, instale todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```
    *Certifique-se de que seu `requirements.txt` contenha `pandas` e `plotly`.*

4.  **Execute a Pipeline de Análise:**
    Para rodar a análise de dados e gerar os gráficos interativos, execute o script principal:
    ```bash
    python src/analise.py
    ```
    *Os gráficos serão abertos em seu navegador padrão.*

5.  **Explore o Notebook (Opcional):**
    Para uma exploração interativa e passo a passo da análise, você pode abrir o notebook Jupyter:
    ```bash
    jupyter notebook src/analise_cancelamentos.ipynb
    ```
    *Se você não tiver o Jupyter, instale-o primeiro: `pip install jupyter`.*

---

## 🔍 Análise e Soluções Baseadas nos Dados

Com base na análise exploratória e nos filtros aplicados, identificamos os seguintes padrões e propomos as respectivas soluções:

### 1. Clientes com Múltiplas Ligações ao Call Center
* **Problema Identificado:** Nossos dados mostram que clientes que realizaram **mais de 3 ligações para o call center** possuem uma propensão significativamente maior ao cancelamento. Isso sugere uma falha na resolução de problemas ou na experiência inicial de atendimento.
* **Solução Proposta:**
    * **Melhorar o Sistema de Atendimento:** Implementar treinamento aprofundado para os agentes do call center, focando na **primeira resolução de contato (FCR)** e na empatia. O objetivo é que o cliente se sinta acolhido e tenha suas questões resolvidas eficientemente logo nas primeiras interações.
    * **Monitoramento Ativo e Proativo:** Criar um sistema de monitoramento contínuo para identificar rapidamente clientes que fazem múltiplas ligações ou que reportam insatisfação. Isso pode incluir alertas para gerentes e a implementação de um **contato proativo** por parte da equipe de relacionamento com o cliente, antes que a insatisfação leve ao cancelamento.

### 2. Clientes com Assinatura Mensal
* **Problema Identificado:** Observa-se que clientes com **planos de assinatura mensais** apresentam uma taxa de cancelamento substancialmente mais alta em comparação com clientes de outros planos (anuais, etc.). Isso pode indicar que o valor percebido do serviço é menor para essa modalidade ou que há menos incentivos para a permanência a longo prazo.
* **Solução Proposta:**
    * **Campanhas de Incentivo para Planos Anuais:** Desenvolver campanhas de marketing agressivas e vantajosas para clientes mensais, oferecendo **descontos significativos, bônus ou funcionalidades exclusivas** para a migração para planos anuais. Isso aumenta a fidelidade e o tempo de vida do cliente (LTV).
    * **Otimização do Valor Percebido no Plano Mensal:** Se a migração não for viável, revisar a proposta de valor do plano mensal. Isso pode incluir a adição de pequenos benefícios extras, acesso a conteúdo exclusivo ou a comunicação mais clara dos benefícios já existentes, buscando **aumentar a satisfação e reduzir a percepção de alto custo** para um compromisso de curto prazo.

---

## 🤝 Contribuições

Sinta-se à vontade para abrir `issues` ou enviar `pull requests` se tiver sugestões de melhorias ou encontrar algum problema.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.