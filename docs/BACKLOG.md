# BACKLOG — Tarefas por Fase

**Legenda:** ⬜ Pendente · 🔄 Em andamento · ✅ Concluído

---

## Setup Inicial

| # | Tarefa | Status |
|---|---|---|
| S1 | Criar repositório GitHub público | ✅ |
| S2 | Criar branch `develop` a partir de `main` | ✅ |
| S3 | Criar estrutura de pastas do projeto | ✅ |
| S4 | Mover CSV para `data/manutencao_preditiva.csv` | ✅ |
| S5 | Primeiro commit com estrutura inicial na `develop` | ✅ |

---

## Fase 1 — Análise Exploratória (EDA)

**Branch:** `feature/eda`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 1.1 | `df.shape` — dimensões do dataset | ✅ | ✅ |
| 1.2 | `df.dtypes` — tipos de dados | ✅ | ✅ |
| 1.3 | `df.describe()` — resumo estatístico | ✅ | ✅ |
| 1.4 | Gráfico 1: Histograma das variáveis contínuas | ✅ | ✅ |
| 1.5 | Gráfico 2: Barras da distribuição de `falha_maquina` | ✅ | ✅ |
| 1.6 | Gráfico 3: Heatmap de correlação de Pearson | ✅ | ✅ |
| 1.7 | Célula de texto interpretativa (análise dos padrões) | ✅ | ✅ |
| 1.8 | Gráfico 4: Scatter RPM × Torque por classe | ➕ | ✅ |
| 1.9 | Gráfico 5: Boxplot das variáveis por classe | ➕ | ✅ |
| 1.10 | Gráfico 6: Countplot do tipo de máquina por classe | ➕ | ✅ |
| 1.11 | Gráfico 7: Violinplot do desgaste por classe | ➕ | ✅ |
| 1.12 | Cálculo de skewness com NumPy | ➕ | ✅ |
| 1.13 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 2 — Limpeza e Tratamento (Data Prep)

**Branch:** `feature/data-prep`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 2.1 | Identificar e remover duplicatas | ✅ | ✅ |
| 2.2 | Mapear valores ausentes por coluna | ✅ | ✅ |
| 2.3 | Verificar distribuição das colunas com NaN | ✅ | ✅ |
| 2.4 | Imputar com média ou mediana + justificativa textual | ✅ | ✅ |
| 2.5 | Boxplots de todas as variáveis explicativas | ✅ | ✅ |
| 2.6 | Gráfico 8: Histograma antes/depois da imputação | ➕ | ✅ |
| 2.7 | Gráfico 9: Heatmap de valores ausentes | ➕ | ✅ |
| 2.8 | Cálculo de limites de outlier com NumPy (IQR) | ➕ | ✅ |
| 2.9 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 3 — Feature Engineering

**Branch:** `feature/feature-engineering`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 3.1 | Criar `potencia = velocidade_rotacao_rpm * torque_nm` | ✅ | ✅ |
| 3.2 | Validar: `df['potencia'].isnull().sum() == 0` | ✅ | ✅ |
| 3.3 | Célula de texto explicando a interpretação física | ✅ | ✅ |
| 3.4 | Gráfico 10: Histograma + KDE da variável `potencia` | ➕ | ✅ |
| 3.5 | Gráfico 11: Scatter `potencia` × `desgaste` por classe | ➕ | ✅ |
| 3.6 | Estatísticas da nova variável com NumPy | ➕ | ✅ |
| 3.7 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 4 — Divisão e Balanceamento

**Branch:** `feature/split-balance`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 4.1 | Definir X (preditoras) e y (`falha_maquina`) | ✅ | ✅ |
| 4.2 | Remover colunas não-preditoras de X | ✅ | ✅ |
| 4.3 | `train_test_split` 80/20 com `stratify=y` | ✅ | ✅ |
| 4.4 | Verificar proporção de classes no treino e teste | ✅ | ✅ |
| 4.5 | Aplicar SMOTE **somente** no `X_train` / `y_train` | ✅ | ✅ |
| 4.6 | Confirmar que `X_test` não passou pelo SMOTE | ✅ | ✅ |
| 4.7 | Gráfico 12: Barras antes/depois do SMOTE | ➕ | ✅ |
| 4.8 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 5 — Escalonamento (StandardScaler)

**Branch:** `feature/scaling`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 5.1 | `fit_transform` no `X_train` para KNN | ✅ | ✅ |
| 5.2 | `transform` no `X_test` para KNN | ✅ | ✅ |
| 5.3 | Manter dados da Árvore sem scaling | ✅ | ✅ |
| 5.4 | Célula de texto justificando a ausência de scaling na Árvore | ✅ | ✅ |
| 5.5 | Verificar média ≈ 0 e std ≈ 1 com NumPy | ➕ | ✅ |
| 5.6 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 6 — Ajuste de Hiperparâmetros

**Branch:** `feature/hyperparams`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 6.1 | KNN K=3: acurácia treino e teste | ✅ | ✅ |
| 6.2 | KNN K=5: acurácia treino e teste | ✅ | ✅ |
| 6.3 | KNN K=7: acurácia treino e teste | ✅ | ✅ |
| 6.4 | Árvore max_depth=3: acurácia treino e teste | ✅ | ✅ |
| 6.5 | Árvore max_depth=5: acurácia treino e teste | ✅ | ✅ |
| 6.6 | Árvore max_depth=None: acurácia treino e teste | ✅ | ✅ |
| 6.7 | Célula de texto identificando overfitting | ✅ | ✅ |
| 6.8 | Gráfico 13: Linha K × Acurácia (KNN) | ➕ | ✅ |
| 6.9 | Gráfico 14: Linha max_depth × Acurácia (Árvore) | ➕ | ✅ |
| 6.10 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Fase 7 — Avaliação Final

**Branch:** `feature/evaluation`

| # | Tarefa | Obrigatório | Status |
|---|---|---|---|
| 7.1 | Acurácia final do melhor KNN no teste | ✅ | ✅ |
| 7.2 | Acurácia final da melhor Árvore no teste | ✅ | ✅ |
| 7.3 | Comparação numérica e veredito em texto | ✅ | ✅ |
| 7.4 | Gráfico 15: Barras KNN vs Árvore | ➕ | ✅ |
| 7.5 | Exportar `outputs/metricas_finais.json` | ➕ | ✅ |
| 7.6 | Merge na `develop` via PR | ✅ | ⬜ |

---

## Documentação

**Branch:** `docs/readme`

| # | Tarefa | Status |
|---|---|---|
| D1 | Completar `README.md` com link do vídeo | ⬜ |
| D2 | Gerar `requirements.txt` com versões fixas (`pip freeze`) | ⬜ |
| D3 | Merge `develop` → `main` | ⬜ |
| D4 | Submeter links no AVA | ⬜ |

---

_Última revisão: 2026-07-10_
