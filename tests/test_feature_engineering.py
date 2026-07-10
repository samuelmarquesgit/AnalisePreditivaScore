"""
Suite de testes — Fase 3: Feature Engineering
Execução: pytest tests/test_feature_engineering.py -v
"""
import pytest
import pandas as pd
import numpy as np

CSV_PATH = "data/manutencao_preditiva.csv"


@pytest.fixture
def df_preparado():
    """Carrega e prepara o dataset (imputação + feature engineering)."""
    df = pd.read_csv(CSV_PATH)
    for col in ["temperatura_ar_k", "temperatura_processo_k",
                "velocidade_rotacao_rpm", "torque_nm"]:
        df[col] = df[col].fillna(df[col].median())
    df["potencia"] = df["velocidade_rotacao_rpm"] * df["torque_nm"]
    return df


def test_coluna_potencia_existe(df_preparado):
    """DataFrame deve conter a coluna 'potencia'."""
    assert "potencia" in df_preparado.columns


def test_potencia_sem_nulos(df_preparado):
    """Coluna 'potencia' não deve conter valores nulos."""
    assert df_preparado["potencia"].isnull().sum() == 0


def test_potencia_formula_correta(df_preparado):
    """potencia deve ser igual a rpm * torque para todas as linhas."""
    esperado = df_preparado["velocidade_rotacao_rpm"] * df_preparado["torque_nm"]
    pd.testing.assert_series_equal(
        df_preparado["potencia"].reset_index(drop=True),
        esperado.reset_index(drop=True),
        check_names=False
    )


def test_potencia_valores_positivos(df_preparado):
    """Potência deve ser não-negativa."""
    assert (df_preparado["potencia"] >= 0).all()


def test_numero_colunas_aumentou(df_preparado):
    """Dataset após FE deve ter mais colunas que o original."""
    df_original = pd.read_csv(CSV_PATH)
    assert len(df_preparado.columns) > len(df_original.columns)
