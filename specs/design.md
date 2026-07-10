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

## Parâmetros Fixos (reprodutibilidade)

| Parâmetro | Valor | Onde usar |
|---|---|---|
| `random_state` | 42 | `train_test_split`, `DecisionTreeClassifier`, `SMOTE` |
| `test_size` | 0.2 | `train_test_split` |
| `stratify` | `y` | `train_test_split` |

---

_Última revisão: 2026-07-10_
