# Tasks — Passo a Passo de Implementação

## TASK-01 · Setup do Repositório

1. Criar branch develop: `git checkout -b develop` → `git push origin develop`
2. Mover o CSV para `data/manutencao_preditiva.csv`
3. `git add .` → `git commit -m "inicializa estrutura do projeto"` → `git push origin develop`

---

## TASK-02 · Fase 1 — EDA

**Branch:** `git checkout -b feature/eda`

1. Célula Markdown: `## Fase 1 — Análise Exploratória (EDA)`
2. Importar: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`
3. Carregar CSV: `pd.read_csv('data/manutencao_preditiva.csv')`
4. Exibir `.shape`, `.dtypes`, `.describe()`
5. Plotar Gráficos 1–3 (obrigatórios): histograma, barras, heatmap
6. Plotar Gráficos 4–7 (extras): scatter, boxplot por classe, countplot, violinplot
7. Célula Markdown: análise dos padrões identificados
8. `git commit -m "implementa EDA com describe e 7 gráficos analíticos"`
9. Merge na develop

---

## TASK-03 · Fase 2 — Data Prep

**Branch:** `git checkout -b feature/data-prep`

1. Verificar e remover duplicatas
2. Mapear NaN por coluna com `.isnull().sum()`
3. Plotar Gráfico 9 — heatmap de NaN
4. Calcular skewness com NumPy para decidir média vs mediana
5. Imputar e justificar em texto
6. Plotar Gráfico 8 — antes/depois da imputação
7. Plotar boxplots de outliers (obrigatório) + calcular IQR com NumPy
8. `git commit -m "adiciona limpeza com imputação por <media/mediana> justificada"`
9. Merge na develop

---

## TASK-04 · Fase 3 — Feature Engineering

**Branch:** `git checkout -b feature/feature-engineering`

1. Confirmar que rpm e torque estão sem NaN
2. Criar: `df['potencia'] = df['velocidade_rotacao_rpm'] * df['torque_nm']`
3. Validar: `df['potencia'].isnull().sum() == 0`
4. Plotar Gráficos 10 e 11
5. Estatísticas com NumPy: `np.mean`, `np.max`
6. Célula Markdown: interpretação física
7. `git commit -m "cria coluna potencia em feature engineering"`
8. Merge na develop

---

## TASK-05 · Fase 4 — Split e Balanceamento

**Branch:** `git checkout -b feature/split-balance`

1. Definir colunas a excluir: identificadores + todos os subtipos de falha
2. Separar X e y
3. `train_test_split` com `test_size=0.2`, `stratify=y`, `random_state=42`
4. Verificar proporção com `.value_counts()`
5. `SMOTE().fit_resample(X_train, y_train)` → `X_train_bal, y_train_bal`
6. Plotar Gráfico 12 — antes/depois do SMOTE
7. `git commit -m "aplica SMOTE somente nos dados de treino"`
8. Merge na develop

---

## TASK-06 · Fase 5 — StandardScaler

**Branch:** `git checkout -b feature/scaling`

1. `scaler.fit_transform(X_train_bal)` → `X_train_knn`
2. `scaler.transform(X_test)` → `X_test_knn`
3. Verificar com NumPy: média ≈ 0, std ≈ 1
4. `X_train_tree = X_train_bal` · `X_test_tree = X_test`
5. Célula Markdown: justificativa da ausência de scaling na Árvore
6. `git commit -m "aplica StandardScaler no KNN e justifica ausencia na arvore"`
7. Merge na develop

---

## TASK-07 · Fase 6 — Hiperparâmetros

**Branch:** `git checkout -b feature/hyperparams`

1. Loop KNN K=3,5,7 → registrar acc_treino e acc_teste
2. Plotar Gráfico 13 — linha K × acurácia
3. Loop Árvore depth=3,5,None → registrar acc_treino e acc_teste
4. Plotar Gráfico 14 — linha depth × acurácia
5. Célula Markdown: identificar overfitting e config ideal
6. `git commit -m "adiciona tuning de hiperparametros e graficos de overfitting"`
7. Merge na develop

---

## TASK-08 · Fase 7 — Avaliação Final

**Branch:** `git checkout -b feature/evaluation`

1. Selecionar melhor K e melhor depth
2. `accuracy_score(y_test, y_pred)` para cada modelo
3. Plotar Gráfico 15 — barras KNN vs Árvore
4. Exportar `outputs/metricas_finais.json` com `json.dump`
5. Célula Markdown: veredito com comparação numérica
6. `git commit -m "implementa avaliacao final e exporta metricas em JSON"`
7. Merge na develop

---

## TASK-09 · Documentação Final

**Branches:** `docs/*` — uma branch por arquivo `.md` (`docs/readme`, `docs/docs-architecture`, `docs/specs-tasks` etc.), revisada e commitada individualmente, cada uma mesclada na `develop` via PR

1. Inserir link do vídeo no README.md
2. `pip freeze > requirements.txt` para fixar versões
3. `git commit -m "finaliza README com link do video e atualiza requirements"`
4. Merge de cada `docs/*` na `develop` → `git checkout main` → `git merge develop` → `git push origin main`

---

## TASK-10 · Submissão

1. Gravar vídeo (máx. 7 min) — sem ferramenta de IA
2. Subir no Google Drive em modo leitor público
3. Verificar repositório GitHub público
4. `Restart & Run All` sem erros
5. Submeter links no AVA — **prazo: 17/07/2026 às 22h**

---

_Última revisão: 2026-07-10_
