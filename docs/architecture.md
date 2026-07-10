# Arquitetura — PredictMaint

## Visão Geral do Pipeline

```
[CSV] → [EDA] → [Data Prep] → [Feature Eng.] → [Split]
                                                    │
                                          ┌─────────┴─────────┐
                                     [X_train]           [X_test]
                                          │
                                       [SMOTE]
                                          │
                               ┌──────────┴──────────┐
                          [KNN path]           [Árvore path]
                        [StandardScaler]       [sem scaling]
                               │                     │
                          [KNN K=3,5,7]     [Árvore d=3,5,None]
                               │                     │
                               └──────────┬──────────┘
                                    [Avaliação Final]
                                    [metricas.json]
                                          │
                                    [Auditoria/Model Card]
                                          │
                         ┌────────────────┼────────────────┐
                    [Random Forest]  [XGBoost/LightGBM]  [Comparação Ampliada]
                     (Fase 8, expl.)   (Fase 9, expl.)    (Fase 10, expl.)
```

As três últimas etapas (Auditoria, Fase 8, Fase 9, Fase 10) são uma extensão exploratória — não fazem parte da entrega oficial (Fases 1-7).

---

## Schema do Dataset

| Coluna | Tipo | Papel | Observações |
|---|---|---|---|
| `udi` | int | Identificador | Remover do X |
| `id_produto` | str | Identificador | Remover do X |
| `tipo` | str | Categórica (L/M/H) | Remover do X |
| `temperatura_ar_k` | float | Preditora | Tem NaN |
| `temperatura_processo_k` | float | Preditora | Tem NaN |
| `velocidade_rotacao_rpm` | float | Preditora | Tem NaN |
| `torque_nm` | float | Preditora | Tem NaN |
| `desgaste_ferramenta_min` | int | Preditora | Sem NaN |
| `falha_maquina` | int | **Alvo (y)** | 0 = normal, 1 = falha |
| `falha_twf` | int | Subtipo | **Remover — data leakage** |
| `falha_hdf` | int | Subtipo | **Remover — data leakage** |
| `falha_pwf` | int | Subtipo | **Remover — data leakage** |
| `falha_osf` | int | Subtipo | **Remover — data leakage** |
| `falha_rnf` | int | Subtipo | **Remover — data leakage** |

**Colunas finais em X (6):** `temperatura_ar_k`, `temperatura_processo_k`, `velocidade_rotacao_rpm`, `torque_nm`, `desgaste_ferramenta_min`, `potencia`

---

## Catálogo de Gráficos

| # | Tipo | Fase | Biblioteca | Objetivo |
|---|---|---|---|---|
| 1 | Histograma | EDA | Matplotlib/Seaborn | Distribuição das variáveis contínuas |
| 2 | Barras | EDA | Matplotlib | Desbalanceamento da variável alvo |
| 3 | Heatmap | EDA | Seaborn | Correlação de Pearson |
| 4 | Scatter | EDA | Seaborn | Separabilidade RPM × Torque por classe |
| 5 | Boxplot por classe | EDA | Seaborn | Diferença de distribuição falha vs normal |
| 6 | Countplot | EDA | Seaborn | Taxa de falha por tipo de máquina |
| 7 | Violinplot | EDA | Seaborn | Distribuição do desgaste por classe |
| 8 | Histograma duplo | Data Prep | Matplotlib | Antes/depois da imputação |
| 9 | Heatmap NaN | Data Prep | Seaborn | Localização dos valores ausentes |
| 10 | Histograma + KDE | Feature Eng. | Seaborn | Distribuição da variável `potencia` |
| 11 | Scatter | Feature Eng. | Seaborn | `potencia` × `desgaste` por classe |
| 12 | Barras duplas | Split | Matplotlib | Distribuição antes/depois SMOTE |
| 13 | Linha | Hiperparâmetros | Matplotlib | K × Acurácia (KNN) |
| 14 | Linha | Hiperparâmetros | Matplotlib | max_depth × Acurácia (Árvore) |
| 15 | Barras | Avaliação | Matplotlib | Comparação final KNN vs Árvore |
| 16 | Heatmap duplo | Auditoria | Seaborn | Matrizes de confusão — KNN e Árvore |
| 17 | Barras | Fase 8 (expl.) | Seaborn | KNN vs Árvore vs Random Forest |
| 18 | Barras | Fase 9 (expl.) | Seaborn | XGBoost vs LightGBM |
| 19 | Barras | Fase 10 (expl.) | Seaborn | Comparação final ampliada (5 modelos) |

---

## Decisões de Design

| Decisão | Escolha | Justificativa |
|---|---|---|
| Balanceamento | SMOTE | Gera amostras sintéticas sem descartar dados da maioria |
| Divisão | 80/20 | Padrão do enunciado; suficiente com 10k amostras |
| Estratificação | `stratify=y` | Mantém proporção de classes em treino e teste |
| Reprodutibilidade | `random_state=42` | Qualquer máquina produz o mesmo resultado |
| Caminhos | Relativos | Portabilidade — avaliador consegue rodar sem modificação |
| Modelos exploratórios sem scaling | Random Forest, XGBoost, LightGBM usam `X_train_tree`/`X_test_tree` | São todos baseados em árvore — mesma justificativa da Árvore de Decisão (DT-03 em `steering/tech.md`) |

---

_Última revisão: 2026-07-10_
