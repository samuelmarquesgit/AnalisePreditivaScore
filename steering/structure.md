# Structure — Estrutura de Pastas e Convenções

## Árvore do Projeto

```
AnalisePreditivaScore/
│
├── notebook.ipynb              ← Pipeline completo (7 fases)
├── requirements.txt            ← Dependências de produção (versões mínimas; fixar com `pip freeze` antes da entrega)
├── requirements-dev.txt        ← Dependências de desenvolvimento
├── pytest.ini                  ← Configuração pytest + cobertura
├── env.example                 ← Template de variáveis (commitar)
├── .env                        ← Configuração local real (NÃO commitar)
├── .gitignore
├── README.md
├── CLAUDE.md                   ← Contexto para Claude Code
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

- `.env` · `outputs/graficos/` · `outputs/coverage_html/` · `__pycache__/` · `.ipynb_checkpoints/`

---

_Última revisão: 2026-07-10_
