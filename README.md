# PredictMaint — Pipeline Preditivo de Falhas Industriais

> Projeto Avaliativo — Módulo 1 · Desenvolvimento de IA para Análise Preditiva

---

## Problema

Um parque fabril monitorado por sensores necessita prever quebras mecânicas nos equipamentos para evitar paradas na linha de produção. A variável alvo é binária: **Falha = 1** (avaria detectada) e **Normal = 0** (funcionamento correto).

## Solução

Pipeline de Ciência de Dados ponta a ponta com 7 fases estruturadas:

```
EDA → Data Prep → Feature Engineering → Split/Balanceamento
    → Escalonamento → Ajuste de Hiperparâmetros → Avaliação Final
```

Dois modelos são comparados — **KNN** e **Árvore de Decisão** — e o de maior acurácia no conjunto de teste é recomendado para produção.

---

## Tecnologias

| Categoria | Biblioteca |
|---|---|
| Manipulação de dados | `pandas`, `numpy` |
| Visualização | `matplotlib`, `seaborn` |
| Machine Learning | `scikit-learn` |
| Balanceamento | `imbalanced-learn` |
| Exportação de métricas | `json` (stdlib) |
| Testes | `pytest` |

---

## Estrutura do Projeto

```
AnalisePreditivaScore/
├── notebook.ipynb          ← pipeline completo (7 fases)
├── requirements.txt        ← dependências de produção
├── requirements-dev.txt    ← dependências de desenvolvimento
├── data/
│   └── manutencao_preditiva.csv
├── outputs/
│   ├── graficos/
│   └── metricas_finais.json
├── docs/                   ← documentação técnica
├── specs/                  ← especificações e tasks
├── steering/               ← direcionamento estratégico
└── tests/                  ← suite pytest
```

---

## Como Executar

### 1. Clone o repositório
```bash
git clone git@github.com:samuelmarquesgit/AnalisePreditivaScore.git
cd AnalisePreditivaScore
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Abra o notebook
```bash
jupyter notebook notebook.ipynb
```

### 4. Execute todas as células em ordem
`Kernel → Restart & Run All`

> **Atenção:** o CSV deve estar em `data/manutencao_preditiva.csv`. Não altere os caminhos relativos.

---

## Rodar os Testes

```bash
pip install -r requirements-dev.txt
pytest --cov=. --cov-report=html
```

---

## Demonstração

🎥 [Assista à demonstração](LINK_DO_VIDEO_AQUI)

---

## Melhorias Possíveis

- Testar algoritmos adicionais (Random Forest, XGBoost, LightGBM)
- Aplicar `GridSearchCV` para busca automática de hiperparâmetros
- Substituir acurácia por **F1-score** e **AUC-ROC** (mais adequadas para dados desbalanceados)
- Expor o modelo via API REST (FastAPI)
- Implementar monitoramento de *Data Drift* em produção

---

## Autor

**Samuel Marques**  
Módulo 1 — Semana 14 · Prazo: 17/07/2026

---

_Última revisão: 2026-07-09_
