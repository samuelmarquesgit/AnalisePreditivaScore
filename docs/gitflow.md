# Git Flow — Convenções e Branching Strategy

## Estrutura de Branches

```
main
└── develop
    ├── feature/eda
    ├── feature/data-prep
    ├── feature/feature-engineering
    ├── feature/split-balance
    ├── feature/scaling
    ├── feature/hyperparams
    ├── feature/evaluation
    ├── feature/random-forest       (Fase 8, exploratório)
    ├── feature/boosting            (Fase 9, exploratório)
    ├── feature/comparacao-ampliada (Fase 10, exploratório)
    ├── chore/setup-inicial
    └── docs/*
        ├── docs/readme
        ├── docs/docs-architecture
        ├── docs/docs-automation-workflow
        ├── docs/docs-gitflow
        ├── docs/docs-roadmap
        ├── docs/docs-technologies
        ├── docs/docs-test-report
        ├── docs/docs-prd
        ├── docs/docs-backlog
        ├── docs/docs-arquitetura-mmd
        ├── docs/specs-tasks
        ├── docs/specs-design
        ├── docs/specs-requirements
        ├── docs/steering-product
        ├── docs/steering-structure
        ├── docs/steering-tech
        ├── docs/github-pr-template
        ├── docs/github-issue-bug-report
        ├── docs/github-issue-feature-request
        ├── docs/sql-schema
        └── docs/auditoria-model-card
```

## Regras

| Regra | Detalhe |
|---|---|
| `main` | Código final entregue — apenas 1 merge (no fim) |
| `develop` | Branch de integração — recebe merges das features |
| `feature/*` | Uma branch por fase do notebook |
| `docs/*` | Uma branch por arquivo `.md` do repositório, nome `docs/<pasta>-<arquivo>` |
| Não excluir branches | Manter todas após o PR para histórico |
| PR sempre para `develop` | Nunca fazer merge direto na `main` durante o desenvolvimento |

## Sequência de Comandos

```bash
# Configuração inicial
git checkout -b develop
git push origin develop

# Fluxo de feature
git checkout develop
git checkout -b feature/eda
# ... desenvolve a Fase 1 ...
git add notebook.ipynb
git commit -m "implementa EDA com describe e 7 gráficos analíticos"
git checkout develop
git merge feature/eda
git push origin develop

# Repetir para cada fase...

# Merge final para main
git checkout main
git merge develop
git push origin main

# Fluxo de docs (um por arquivo .md)
git checkout develop
git checkout -b docs/docs-architecture
# ... revisa e ajusta docs/architecture.md ...
git add docs/architecture.md
git commit -m "docs: revisa docs/architecture.md"
git checkout develop
git merge docs/docs-architecture
git push origin develop
```

## Padrão de Mensagens de Commit

| ✅ Correto | ❌ Errado |
|---|---|
| `implementa EDA com 7 gráficos` | `EDA foi implementada` |
| `adiciona imputação por mediana com justificativa` | `data prep done` |
| `cria coluna potencia em feature engineering` | `feature engineering` |
| `aplica SMOTE somente nos dados de treino` | `balanceamento` |
| `corrige fit_transform aplicado no teste` | `fix` |
| `adiciona gráficos de tuning KNN e árvore` | `gráficos` |

---

_Última revisão: 2026-07-10_
