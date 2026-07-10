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
```

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

---

## Decisões de Design

| Decisão | Escolha | Justificativa |
|---|---|---|
| Balanceamento | SMOTE | Gera amostras sintéticas sem descartar dados da maioria |
| Divisão | 80/20 | Padrão do enunciado; suficiente com 10k amostras |
| Estratificação | `stratify=y` | Mantém proporção de classes em treino e teste |
| Reprodutibilidade | `random_state=42` | Qualquer máquina produz o mesmo resultado |
| Caminhos | Relativos | Portabilidade — avaliador consegue rodar sem modificação |

---

_Última revisão: 2026-07-09_
