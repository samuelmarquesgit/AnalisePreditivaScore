# Stack Técnica — PredictMaint

## Linguagem e Runtime

| Tecnologia | Versão mínima | Papel |
|---|---|---|
| Python | 3.10+ | Linguagem principal |
| Jupyter Notebook | 7.0+ | Ambiente de desenvolvimento interativo |

## Bibliotecas de Produção

| Biblioteca | Versão mínima | Papel no projeto |
|---|---|---|
| `pandas` | 2.0 | Leitura do CSV, limpeza, transformação, seleção de colunas |
| `numpy` | 1.24 | Cálculos estatísticos (IQR, percentis, skewness), vetorização |
| `matplotlib` | 3.7 | Histogramas, barras, linhas de tuning, subplots |
| `seaborn` | 0.12 | Heatmaps, scatter, boxplot, violinplot, countplot, KDE |
| `scikit-learn` | 1.3 | Split, StandardScaler, KNN, Árvore de Decisão, accuracy_score |
| `imbalanced-learn` | 0.11 | SMOTE para balanceamento da classe minoritária |
| `json` | stdlib | Exportação de métricas finais para arquivo |

## Bibliotecas de Desenvolvimento

| Biblioteca | Papel |
|---|---|
| `pytest` | Execução da suite de testes |
| `pytest-cov` | Cobertura de código com relatório HTML |
| `nbqa` | Aplicar linters em notebooks |
| `nbmake` | Executa o notebook como teste pytest (`pytest --nbmake`) |

## Referência de Imports por Fase

| Fase | Imports |
|---|---|
| 1 — EDA | `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn` |
| 2 — Data Prep | `pandas`, `numpy` |
| 3 — Feature Eng. | `pandas`, `numpy` |
| 4 — Split/Balance | `sklearn.model_selection`, `imblearn.over_sampling` |
| 5 — Scaling | `sklearn.preprocessing` |
| 6 — Modelos | `sklearn.neighbors`, `sklearn.tree`, `sklearn.metrics` |
| 7 — Avaliação | `sklearn.metrics`, `json`, `os` |

---

_Última revisão: 2026-07-09_
