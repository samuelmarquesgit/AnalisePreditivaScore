# Test Report — PredictMaint

**Data de execução:** _preencher após rodar pytest_  
**Comando:** `pytest --cov=. --cov-report=term-missing`

---

## Resumo

| Total | Passou | Falhou | Cobertura |
|---|---|---|---|
| — | — | — | — |

---

## Resultados por Arquivo

### `tests/test_data_prep.py`

| Teste | Status |
|---|---|
| `test_csv_carrega_corretamente` | — |
| `test_dataset_tem_linhas_suficientes` | — |
| `test_variavel_alvo_binaria` | — |
| `test_sem_duplicatas_apos_limpeza` | — |
| `test_colunas_com_nan_identificadas` | — |
| `test_sem_nulos_apos_imputacao` | — |
| `test_iqr_calculado_corretamente` | — |

### `tests/test_feature_engineering.py`

| Teste | Status |
|---|---|
| `test_coluna_potencia_existe` | — |
| `test_potencia_sem_nulos` | — |
| `test_potencia_formula_correta` | — |
| `test_potencia_valores_positivos` | — |
| `test_numero_colunas_aumentou` | — |

### `tests/test_model_evaluation.py`

| Teste | Status |
|---|---|
| `test_json_exportado_existe` | — |
| `test_json_estrutura_valida` | — |
| `test_acuracia_knn_acima_minimo` | — |
| `test_acuracia_arvore_acima_minimo` | — |
| `test_modelo_selecionado_nao_vazio` | — |

---

## Cobertura HTML

Relatório completo: `outputs/coverage_html/index.html`

---

## Nota sobre a extensão exploratória

A suite `tests/` cobre apenas as Fases 1-7 (entrega oficial). A Auditoria do Modelo e as Fases 8-10 (Random Forest, XGBoost, LightGBM) são exploratórias e não têm testes dedicados — seus artefatos (`outputs/auditoria_metricas.json`, `outputs/metricas_modelos_avancados.json`) podem ser inspecionados manualmente ou via `docs/auditoria/model_card.md`.

---

_Última revisão: 2026-07-10_
