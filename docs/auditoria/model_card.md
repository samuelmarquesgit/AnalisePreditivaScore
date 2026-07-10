# Model Card — PredictMaint

Documentação de auditoria do modelo, no formato Model Card (Mitchell et al., 2019), cobrindo uso pretendido, desempenho, limitações e riscos.

## Detalhes do Modelo

| Campo | Valor |
|---|---|
| Nome | PredictMaint — Classificador de Falha Mecânica |
| Tipo | Classificação binária |
| Algoritmos comparados | K-Nearest Neighbors (KNN) e Árvore de Decisão |
| Modelo selecionado | **Árvore de Decisão** (`max_depth=None`) |
| Versão dos dados | `data/manutencao_preditiva.csv` — 10.000 linhas, 14 colunas |
| Data de treino | 2026-07-10 |
| Reprodutibilidade | `random_state=42` em `train_test_split`, `SMOTE` e `DecisionTreeClassifier` |

## Uso Pretendido

- **Uso primário:** apoiar equipes de manutenção industrial a antecipar falhas mecânicas em equipamentos monitorados por sensores, priorizando inspeção preventiva.
- **Usuários-alvo:** equipe de manutenção industrial, gestores de produção.
- **Fora do escopo:** decisão automática de parada de equipamento sem revisão humana; uso em equipamentos com perfil de sensor diferente do dataset de treino; ambientes de produção sem monitoramento de data drift.

## Dados de Treino e Teste

| Partição | Linhas | Classe 0 (Normal) | Classe 1 (Falha) |
|---|---|---|---|
| Treino (antes do SMOTE) | 8.000 | 7.729 (96,6%) | 271 (3,4%) |
| Treino (depois do SMOTE) | 15.458 | 7.729 (50%) | 7.729 (50%) |
| Teste (sem resampling) | 2.000 | ~1.932 (96,6%) | ~68 (3,4%) |

O conjunto de teste **não** passou por SMOTE nem por `fit` de nenhum transformador — simula dados nunca vistos pelo modelo.

## Métricas de Desempenho

### Acurácia (Fase 7)

| Modelo | Acurácia treino | Acurácia teste |
|---|---|---|
| KNN (k=3) | 0,9578 | 0,9080 |
| Árvore de Decisão (max_depth=None) | 0,9896 | 0,9370 |

### Matriz de Confusão, Precisão, Recall e F1 (Auditoria)

| Modelo | Precisão | Recall | F1-score |
|---|---|---|---|
| KNN | 0,2264 | **0,7059** | 0,3429 |
| Árvore de Decisão | 0,3041 | 0,6618 | 0,4167 |

**Matriz de confusão — KNN** (linhas=real, colunas=previsto):

|  | Previsto Normal | Previsto Falha |
|---|---|---|
| **Real Normal** | 1.768 | 164 |
| **Real Falha** | 20 | 48 |

**Matriz de confusão — Árvore de Decisão:**

|  | Previsto Normal | Previsto Falha |
|---|---|---|
| **Real Normal** | 1.829 | 103 |
| **Real Falha** | 23 | 45 |

> ⚠️ **Achado da auditoria — tensão entre acurácia e recall:** o modelo selecionado na Fase 7 foi a Árvore de Decisão, por ter a maior acurácia de teste (0,9370 vs 0,9080). Porém, ao medir especificamente a classe Falha, o **KNN tem recall maior** (0,7059 vs 0,6618) — captura 48 das 68 falhas reais do teste, contra 45 da Árvore, e comete **menos falsos negativos** (20 vs 23). Como esta seção de Análise de Risco argumenta que o falso negativo é o erro mais caro no domínio de manutenção preditiva, **o critério de seleção "maior acurácia" usado na Fase 7 não é o mesmo que "menor risco de falha não detectada"** — os dois modelos empatam em não ser claramente superiores um ao outro, dependendo da métrica priorizada. Isso não invalida a escolha da Fase 7 (acurácia era o critério definido no enunciado), mas é uma limitação a declarar explicitamente para quem for usar o modelo em produção.

### Desempenho por Tipo de Máquina (L/M/H)

| Tipo | n (teste) | Acurácia KNN | Acurácia Árvore |
|---|---|---|---|
| L | 1.170 | 0,9103 | 0,9342 |
| M | 616 | 0,9091 | 0,9399 |
| H | 214 | 0,8925 | 0,9439 |

O modelo é consistente entre os três tipos de máquina — nenhum subgrupo mostra queda de acurácia desproporcional. A Árvore de Decisão mantém desempenho estável (93-94%) em L, M e H; o KNN varia um pouco mais, com o pior resultado no tipo H (89,25%, também o subgrupo com menor `n` no teste, 214 amostras).

## Análise de Risco

- **Falso negativo** (falha real prevista como normal): risco de segurança e parada não planejada — o custo mais crítico neste domínio. O **recall da classe Falha (1)** é a métrica mais relevante para avaliar esse risco, mais do que a acurácia agregada.
- **Falso positivo** (normal previsto como falha): custo de manutenção preventiva desnecessária — menos crítico, mas com impacto operacional se recorrente.
- **Desbalanceamento de classes** (~97%/3%): mitigado com SMOTE apenas no treino; a acurácia isolada é uma métrica enganosa nesse cenário (um classificador trivial que sempre prevê "Normal" atingiria ~97% de acurácia sem detectar nenhuma falha).

## Limitações Conhecidas

- Modelo treinado com dados sintéticos/simulados de um único dataset — desempenho em ambiente real não verificado.
- Sem monitoramento de *data drift* em produção (ver `steering/product.md` — melhoria futura).
- Hiperparâmetros ajustados por busca manual (K e `max_depth` fixos), não por `GridSearchCV`.
- Métrica de seleção do modelo final é a acurácia de teste; não pondera custo assimétrico entre falso positivo e falso negativo.

## Considerações Éticas

- Decisões de manutenção com base neste modelo devem manter supervisão humana — o modelo é uma ferramenta de priorização, não um substituto do julgamento técnico.
- Nenhum dado pessoal é utilizado — apenas leituras de sensores de equipamento.

---

_Última revisão: 2026-07-10_
