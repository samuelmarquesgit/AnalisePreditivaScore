# Automation Workflow — Fluxos de Execução

## Fluxo Principal (notebook completo)

```
1. Abrir terminal na raiz do projeto
2. pip install -r requirements.txt
3. jupyter notebook notebook.ipynb
4. Kernel → Restart & Run All
5. Verificar que todas as células executam sem erro
6. Verificar que outputs/metricas_finais.json foi gerado
```

## Fluxo de Testes

```
1. pip install -r requirements-dev.txt
2. pytest
3. Abrir outputs/coverage_html/index.html para relatório visual
```

## Fluxo SMOTE (detalhe Fase 4)

```
X, y definidos
    ↓
train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    ↓
    ├── X_train, y_train  →  SMOTE().fit_resample()  →  X_train_bal, y_train_bal
    └── X_test, y_test    →  (intocados — simulam dados reais)
```

## Fluxo StandardScaler (detalhe Fase 5)

```
X_train_bal
    ↓
scaler = StandardScaler()
scaler.fit_transform(X_train_bal)  →  X_train_knn   (aprende μ e σ aqui)
scaler.transform(X_test)           →  X_test_knn    (aplica os mesmos μ e σ)

X_train_bal  →  X_train_tree  (sem modificação)
X_test       →  X_test_tree   (sem modificação)
```

## Fluxo de Tuning (detalhe Fase 6)

```
Para cada K em [3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=K)
    knn.fit(X_train_knn, y_train_bal)
    acc_treino = accuracy_score(y_train_bal, knn.predict(X_train_knn))
    acc_teste  = accuracy_score(y_test, knn.predict(X_test_knn))
    registrar(K, acc_treino, acc_teste)

Para cada depth em [3, 5, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train_tree, y_train_bal)
    acc_treino = accuracy_score(y_train_bal, tree.predict(X_train_tree))
    acc_teste  = accuracy_score(y_test, tree.predict(X_test_tree))
    registrar(depth, acc_treino, acc_teste)
```

## Fluxo de Exportação JSON (detalhe Fase 7)

```python
metricas = {
    "melhor_knn":    {"k": <K_vencedor>,     "acuracia_teste": <valor>},
    "melhor_arvore": {"max_depth": <depth>,  "acuracia_teste": <valor>},
    "modelo_selecionado": "<nome>",
    "justificativa": "<texto>"
}
with open("outputs/metricas_finais.json", "w", encoding="utf-8") as f:
    json.dump(metricas, f, ensure_ascii=False, indent=2)
```

## Fluxo de Modelos Avançados — Fases 8-10 (exploratório)

```
X_train_tree, y_train_bal (mesmos dados da Árvore — sem scaling)
    ↓
    ├── RandomForestClassifier(n_estimators=100, random_state=42)      → Fase 8
    ├── XGBClassifier(random_state=42, eval_metric='logloss')          → Fase 9
    └── LGBMClassifier(random_state=42, verbose=-1)                    → Fase 9
    ↓
accuracy_score(treino) e accuracy_score(teste) para cada um
    ↓
Comparação com KNN e Árvore (Fase 10) → outputs/metricas_modelos_avancados.json
```

## Fluxo de Auditoria (Model Card, exploratório)

```
knn_final, arvore_final (modelos da Fase 7)
    ↓
predict(X_test_knn) / predict(X_test_tree)
    ↓
confusion_matrix, precision_score, recall_score, f1_score
    ↓
desempenho por tipo de máquina (L/M/H) via df.loc[X_test.index, 'tipo']
    ↓
outputs/auditoria_metricas.json → docs/auditoria/model_card.md
```

## Fluxo Git por Feature

```bash
git checkout develop
git checkout -b feature/<nome-da-fase>
# ... desenvolve ...
git add notebook.ipynb
git commit -m "implementa <descrição>"
git checkout develop
git merge feature/<nome-da-fase>
# NÃO excluir a branch
```

---

_Última revisão: 2026-07-10_
