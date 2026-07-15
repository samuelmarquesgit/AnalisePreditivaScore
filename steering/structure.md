# Structure — Estrutura de Pastas e Convenções

## Árvore do Projeto

```
PredictMaint/
│
├── notebook.ipynb              ← Pipeline: 7 fases obrigatórias + auditoria e Fases 8-10 (exploratório)
├── requirements.txt            ← Dependências de produção (versões mínimas; fixar com `pip freeze` antes da entrega)
├── requirements-dev.txt        ← Dependências de desenvolvimento
├── pytest.ini                  ← Configuração pytest + cobertura
├── env.example                 ← Template de variáveis (commitar)
├── .env                        ← Configuração local real (NÃO commitar)
├── .gitignore
├── README.md
│
├── data/
│   └── manutencao_preditiva.csv
│
├── tests/
│   ├── test_data_prep.py
│   ├── test_feature_engineering.py
│   └── test_model_evaluation.py
│
├── docs/
│   ├── PRD.md
│   ├── BACKLOG.md
│   ├── architecture.md
│   ├── automation_workflow.md
│   ├── gitflow.md
│   ├── roadmap.md
│   ├── technologies.md
│   ├── test_report.md
│   ├── arquitetura.mmd
│   ├── auditoria/
│   │   └── model_card.md   ← Model Card (exploratório)
│   ├── postman/
│   └── pdf/
│       ├── anotações do Departamento de Engenharia.docx
│       └── Conhecendo Alguns Modelos de Machine Learning.pdf
│
├── specs/
│   ├── requirements.md
│   ├── tasks.md
│   └── design.md
│
├── steering/
│   ├── product.md
│   ├── structure.md
│   └── tech.md
│
├── sql/
│   └── schema.sql
│
├── outputs/
│   ├── graficos/
│   ├── metricas_finais.json
│   ├── auditoria_metricas.json          ← exploratório
│   ├── metricas_modelos_avancados.json  ← exploratório
│   └── coverage_html/
│
└── .github/
    ├── pull_request_template.md
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

## Convenções

| Tipo | Convenção | Exemplo |
|---|---|---|
| Branches | kebab-case com prefixo | `feature/eda`, `docs/readme` |
| Commits | imperativo em português | `implementa EDA com 7 gráficos` |
| Variáveis Python | snake_case | `X_train_knn`, `acc_teste` |

## O que NÃO commitar

- `.env` · `docs/anotacoes.txt` · `__pycache__/` · `.ipynb_checkpoints/`

> `outputs/` (gráficos, `coverage_html/` e JSONs de métricas) **é versionado propositalmente** — evidencia os resultados no GitHub sem exigir que o avaliador rode o notebook.

---

_Última revisão: 2026-07-10 (removida referência a CLAUDE.md, não versionado a pedido do autor)_
