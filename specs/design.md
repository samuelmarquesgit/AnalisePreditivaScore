# Design — Decisões de Interface e Contratos

## Contrato de Dados — Entrada

```
Arquivo: data/manutencao_preditiva.csv
Colunas esperadas (14):
  udi, id_produto, tipo,
  temperatura_ar_k, temperatura_processo_k,
  velocidade_rotacao_rpm, torque_nm, desgaste_ferramenta_min,
  falha_maquina,
  falha_twf, falha_hdf, falha_pwf, falha_osf, falha_rnf
```

## Contrato de Dados — X (preditoras)

```
Colunas incluídas em X (6):
  temperatura_ar_k, temperatura_processo_k,
  velocidade_rotacao_rpm, torque_nm,
  desgaste_ferramenta_min, potencia

Colunas EXCLUÍDAS de X:
  udi, id_produto, tipo          ← identificadores/categórica
  falha_twf, falha_hdf,
  falha_pwf, falha_osf, falha_rnf ← data leakage
  falha_maquina                  ← é o y
```

## Contrato de Dados — Saída JSON

```json
{
    "melhor_knn": {
        "k": <int>,
        "acuracia_treino": <float>,
        "acuracia_teste": <float>
    },
    "melhor_arvore": {
        "max_depth": <int | null>,
        "acuracia_treino": <float>,
        "acuracia_teste": <float>
    },
    "modelo_selecionado": "<string>",
    "justificativa": "<string>"
}
```

## Contrato de Dados — Saída JSON da Auditoria (exploratório)

```json
{
    "confusion_matrix": {"knn": [[int, int], [int, int]], "arvore": [[int, int], [int, int]]},
    "metricas_extras": {
        "knn":    {"precisao": <float>, "recall": <float>, "f1": <float>},
        "arvore": {"precisao": <float>, "recall": <float>, "f1": <float>}
    },
    "desempenho_por_tipo": [
        {"tipo": "<L|M|H>", "n": <int>, "acc_knn": <float>, "acc_arvore": <float>}
    ]
}
```
Arquivo: `outputs/auditoria_metricas.json`

## Contrato de Dados — Saída JSON Ampliada (exploratório)

```json
{
    "resultados": {
        "knn": {"acuracia_treino": <float>, "acuracia_teste": <float>},
        "arvore_decisao": {"acuracia_treino": <float>, "acuracia_teste": <float>},
        "random_forest": {"acuracia_treino": <float>, "acuracia_teste": <float>},
        "xgboost": {"acuracia_treino": <float>, "acuracia_teste": <float>},
        "lightgbm": {"acuracia_treino": <float>, "acuracia_teste": <float>}
    },
    "melhor_modelo": "<string>"
}
```
Arquivo: `outputs/metricas_modelos_avancados.json`

## Nomenclatura de Variáveis

| Variável | Descrição |
|---|---|
| `df` | DataFrame principal |
| `X` / `y` | Preditoras e alvo |
| `X_train`, `y_train` | Partição de treino (80%) |
| `X_test`, `y_test` | Partição de teste (20%) |
| `X_train_bal`, `y_train_bal` | Treino após SMOTE |
| `X_train_knn`, `X_test_knn` | Dados escalonados para KNN |
| `X_train_tree`, `X_test_tree` | Dados originais para Árvore |
| `scaler` | Instância do StandardScaler |
| `y_pred_knn`, `y_pred_arvore` | Predições no teste — usadas na auditoria (exploratório) |
| `cm_knn`, `cm_arvore` | Matrizes de confusão (exploratório) |
| `rf_final`, `xgb_final`, `lgbm_final` | Modelos treinados nas Fases 8-9 (exploratório) |
| `resultados_ampliados`, `melhor_modelo_ampliado` | Comparação dos 5 modelos — Fase 10 (exploratório) |

## Parâmetros Fixos (reprodutibilidade)

| Parâmetro | Valor | Onde usar |
|---|---|---|
| `random_state` | 42 | `train_test_split`, `DecisionTreeClassifier`, `SMOTE`, `RandomForestClassifier`, `XGBClassifier`, `LGBMClassifier` |
| `test_size` | 0.2 | `train_test_split` |
| `stratify` | `y` | `train_test_split` |
| `n_estimators` | 100 | `RandomForestClassifier` (exploratório) |

---

_Última revisão: 2026-07-10_
