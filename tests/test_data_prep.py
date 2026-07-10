"""
Suite de testes — Fase 2: Limpeza e Tratamento de Dados
Execução: pytest tests/test_data_prep.py -v
"""
import pytest
import pandas as pd
import numpy as np

CSV_PATH = "data/manutencao_preditiva.csv"

COLUNAS_ESPERADAS = [
    "udi", "id_produto", "tipo",
    "temperatura_ar_k", "temperatura_processo_k",
    "velocidade_rotacao_rpm", "torque_nm",
    "desgaste_ferramenta_min", "falha_maquina",
    "falha_twf", "falha_hdf", "falha_pwf", "falha_osf", "falha_rnf"
]

COLUNAS_COM_NAN = [
    "temperatura_ar_k",
    "temperatura_processo_k",
    "velocidade_rotacao_rpm",
    "torque_nm"
]


@pytest.fixture
def df_raw():
    """Carrega o dataset bruto."""
    return pd.read_csv(CSV_PATH)


def test_csv_carrega_corretamente(df_raw):
    """CSV deve ter exatamente as 14 colunas esperadas."""
    for col in COLUNAS_ESPERADAS:
        assert col in df_raw.columns, f"Coluna ausente: {col}"


def test_dataset_tem_linhas_suficientes(df_raw):
    """Dataset deve ter pelo menos 5.000 linhas."""
    assert len(df_raw) >= 5000, f"Dataset menor que o esperado: {len(df_raw)} linhas"


def test_variavel_alvo_binaria(df_raw):
    """falha_maquina deve conter apenas 0 e 1."""
    valores = set(df_raw["falha_maquina"].unique())
    assert valores.issubset({0, 1}), f"Valores inesperados: {valores}"


def test_sem_duplicatas_apos_limpeza(df_raw):
    """Após drop_duplicates, não devem existir linhas duplicadas."""
    df_clean = df_raw.drop_duplicates()
    assert df_clean.duplicated().sum() == 0


def test_colunas_com_nan_identificadas(df_raw):
    """As colunas com NaN devem ter pelo menos 1 valor ausente."""
    for col in COLUNAS_COM_NAN:
        assert df_raw[col].isnull().sum() > 0, f"Esperava NaN em {col}"


def test_sem_nulos_apos_imputacao(df_raw):
    """Após imputação com mediana, colunas não devem ter NaN."""
    df = df_raw.copy()
    for col in COLUNAS_COM_NAN:
        df[col] = df[col].fillna(df[col].median())
    for col in COLUNAS_COM_NAN:
        assert df[col].isnull().sum() == 0, f"Ainda há NaN em {col} após imputação"


def test_iqr_calculado_corretamente(df_raw):
    """IQR deve ser positivo para variáveis numéricas."""
    col = "torque_nm"
    dados = df_raw[col].dropna()
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1
    assert iqr > 0, "IQR deve ser maior que zero"
