import pandas as pd
import plotly.express as px

# --- 1. Carregamento e Limpeza de Dados ---
def carregar_e_limpar_dados(caminho_arquivo):
    """
    Carrega o arquivo CSV e realiza as etapas iniciais de limpeza dos dados.

    Args:
        caminho_arquivo (str): O caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: Um DataFrame pandas com os dados limpos.
    """
    try:
        tabela = pd.read_csv("../dados/cancelamentos.csv")
        print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{"../dados/cancelamentos.csv"}' não foi encontrado. Verifique o caminho.")
        return None

    # Remover a coluna 'CustomerID'
    if 'CustomerID' in tabela.columns:
        tabela = tabela.drop(columns="CustomerID")
        print("Coluna 'CustomerID' removida.")
    else:
        print("Coluna 'CustomerID' não encontrada no DataFrame.")

    # Remover linhas com valores ausentes
    linhas_antes_dropna = tabela.shape[0]
    tabela = tabela.dropna()
    linhas_depois_dropna = tabela.shape[0]
    print(f"{linhas_antes_dropna - linhas_depois_dropna} linhas com valores ausentes removidas.")

    return tabela

# --- 2. Análise Exploratória de Dados (EDA) ---
def realizar_eda(tabela):
    """
    Realiza a Análise Exploratória de Dados, exibindo contagens e gerando histogramas.

    Args:
        tabela (pd.DataFrame): O DataFrame a ser analisado.
    """
    if tabela is None:
        print("Não foi possível realizar a EDA. O DataFrame é nulo.")
        return

    print("\n--- Análise Exploratória de Dados (EDA) ---")

    # Contagem de valores para a coluna 'cancelou'
    print("\nContagem de valores para 'cancelou':")
    print(tabela['cancelou'].value_counts())

    print("\nContagem de valores normalizada para 'cancelou':")
    print(tabela['cancelou'].value_counts(normalize=True))

    # Geração de histogramas para cada coluna
    print("\nGerando histogramas para todas as colunas...")
    for coluna in tabela.columns:
        print(f"Exibindo gráfico para a coluna: {coluna}")
        grafico = px.histogram(tabela, x=coluna, color="cancelou", text_auto=True,
                               title=f'Distribuição de {coluna} por Cancelamento')
        grafico.show()
    print("Geração de histogramas concluída.")

# --- 3. Filtragem e Análise Final ---
def aplicar_filtros_e_analisar(tabela):
    """
    Aplica filtros específicos aos dados e exibe a contagem final de cancelamentos.

    Args:
        tabela (pd.DataFrame): O DataFrame a ser filtrado e analisado.
    """
    if tabela is None:
        print("Não foi possível aplicar filtros. O DataFrame é nulo.")
        return

    print("\n--- Aplicação de Filtros e Análise Final ---")

    # Filtrar 'ligacoes_callcenter'
    ligacoes_antes = tabela.shape[0]
    tabela_ligacoes = tabela[tabela['ligacoes_callcenter'] <= 4].copy()
    ligacoes_depois = tabela_ligacoes.shape[0]
    print(f"Filtrando 'ligacoes_callcenter' (<= 4): {ligacoes_antes - ligacoes_depois} linhas removidas.")

    # Filtrar 'duracao_contrato'
    duracao_antes = tabela_ligacoes.shape[0]
    tabela_final = tabela_ligacoes[tabela_ligacoes['duracao_contrato'] != 'Monthly'].copy()
    duracao_depois = tabela_final.shape[0]
    print(f"Filtrando 'duracao_contrato' (diferente de 'Monthly'): {duracao_antes - duracao_depois} linhas removidas.")

    print("\nResultado final após os filtros (contagem normalizada de 'cancelou'):")
    if not tabela_final.empty:
        print(tabela_final['cancelou'].value_counts(normalize=True))
    else:
        print("O DataFrame final está vazio após a aplicação dos filtros.")

# --- Execução da Pipeline ---
if __name__ == "__main__":
    caminho_do_csv = '../dados/cancelamentos.csv' # Certifique-se de que este caminho está correto

    # Passo 1: Carregar e limpar os dados
    df_cancelamentos = carregar_e_limpar_dados(caminho_do_csv)

    if df_cancelamentos is not None:
        # Passo 2: Realizar a Análise Exploratória de Dados
        realizar_eda(df_cancelamentos)

        # Passo 3: Aplicar filtros e realizar a análise final
        aplicar_filtros_e_analisar(df_cancelamentos.copy()) # Usamos .copy() para não alterar o DF original da EDA
    else:
        print("\nProcesso interrompido devido a erro no carregamento/limpeza dos dados.")