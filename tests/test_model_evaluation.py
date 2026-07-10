"""
Suite de testes — Fase 7: Avaliação Final
Testa a existência e validade dos artefatos gerados pelo pipeline.
Execução: pytest tests/test_model_evaluation.py -v

ATENÇÃO: execute o notebook completo antes de rodar esta suite.
"""
import pytest
import json
import os

JSON_PATH = "outputs/metricas_finais.json"


def test_json_exportado_existe():
    """O arquivo de métricas finais deve existir após execução do notebook."""
    assert os.path.exists(JSON_PATH), (
        f"Arquivo {JSON_PATH} não encontrado. "
        "Execute o notebook completo antes de rodar os testes."
    )


def test_json_estrutura_valida():
    """O JSON deve conter as chaves esperadas."""
    if not os.path.exists(JSON_PATH):
        pytest.skip("JSON não gerado ainda")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        metricas = json.load(f)
    assert "melhor_knn" in metricas
    assert "melhor_arvore" in metricas
    assert "modelo_selecionado" in metricas
    assert "justificativa" in metricas


def test_acuracia_knn_acima_minimo():
    """Acurácia do melhor KNN no teste deve ser superior a 80%."""
    if not os.path.exists(JSON_PATH):
        pytest.skip("JSON não gerado ainda")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        metricas = json.load(f)
    acc = metricas["melhor_knn"]["acuracia_teste"]
    assert acc > 0.80, f"Acurácia KNN abaixo do esperado: {acc:.4f}"


def test_acuracia_arvore_acima_minimo():
    """Acurácia da melhor Árvore no teste deve ser superior a 80%."""
    if not os.path.exists(JSON_PATH):
        pytest.skip("JSON não gerado ainda")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        metricas = json.load(f)
    acc = metricas["melhor_arvore"]["acuracia_teste"]
    assert acc > 0.80, f"Acurácia Árvore abaixo do esperado: {acc:.4f}"


def test_modelo_selecionado_nao_vazio():
    """Campos modelo_selecionado e justificativa não devem estar vazios."""
    if not os.path.exists(JSON_PATH):
        pytest.skip("JSON não gerado ainda")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        metricas = json.load(f)
    assert metricas["modelo_selecionado"] != ""
    assert metricas["justificativa"] != ""
