# PRD — Product Requirements Document
**Projeto:** PredictMaint — Pipeline Preditivo de Falhas Industriais  
**Versão:** 1.0  
**Data:** 07/07/2026  
**Prazo de entrega:** 17/07/2026 às 22h

---

## 1. Visão Geral

### Problema
Um parque fabril monitorado por sensores sofre paradas inesperadas na linha de produção causadas por falhas mecânicas não previstas. Cada parada gera prejuízo operacional e risco à segurança.

### Solução
Sistema de Machine Learning que analisa leituras históricas de sensores (temperatura, rotação, torque, desgaste) e classifica se um equipamento está em risco de falha (**Falha = 1**) ou em operação normal (**Normal = 0**), permitindo manutenção preventiva antes da quebra.

### Tipo de Problema
- **Paradigma:** Aprendizado Supervisionado
- **Tarefa:** Classificação Binária
- **Métrica principal:** Acurácia no conjunto de teste

---

## 2. Objetivos e Critérios de Sucesso

| Objetivo | Critério de Aceite |
|---|---|
| Pipeline reprodutível | Qualquer pessoa com Python consegue rodar `Restart & Run All` sem erros |
| Combate ao overfitting | Gap entre acurácia de treino e teste < 5% no modelo final |
| Balanceamento sem leakage | SMOTE aplicado **somente** no X_train |
| Veredito fundamentado | Conclusão textual com comparação numérica das acurácias |

---

## 3. Escopo

### Dentro do escopo
- Pipeline Python em Jupyter Notebook (`.ipynb`)
- 7 fases documentadas com células de texto interpretativas
- Mínimo 3 gráficos (meta: 15 gráficos)
- Dois modelos: KNN e Árvore de Decisão
- Exportação de métricas para `outputs/metricas_finais.json`
- Repositório GitHub público com branching strategy
- Vídeo de apresentação (máx. 7 min)

### Fora do escopo (entrega oficial)
- Deploy em produção / API REST (listado como melhoria futura)
- Otimização automática de hiperparâmetros (GridSearchCV)

### Extensão exploratória (não obrigatória, Fases 8-10)
- Auditoria do modelo (Model Card em `docs/auditoria/model_card.md`): matriz de confusão, precisão/recall/F1, desempenho por tipo de máquina
- Comparação com Random Forest, XGBoost e LightGBM, com base no material de apoio `docs/pdf/Conhecendo Alguns Modelos de Machine Learning.pdf`
- Esta extensão **não substitui** o veredito oficial da Fase 7 (KNN vs Árvore de Decisão), que continua sendo o critério de avaliação do enunciado

---

## 4. Restrições

| Restrição | Detalhe |
|---|---|
| Código autoral | Escrever o código — Seção 8 do enunciado |
| Caminhos relativos | Proibido usar caminhos absolutos no notebook |
| Prazo | 17/07/2026 às 22h — não aceita alterações pós-entrega |
| Vídeo sem IA | Ferramentas de IA para geração de vídeo são proibidas |

---

## 5. Dataset

| Atributo | Valor |
|---|---|
| Arquivo | `data/manutencao_preditiva.csv` |
| Linhas | ~10.000 |
| Colunas | 14 |
| Variável alvo | `falha_maquina` (0 = normal, 1 = falha) |
| Valores ausentes | Sim — `temperatura_ar_k`, `temperatura_processo_k`, `velocidade_rotacao_rpm`, `torque_nm` |
| Desbalanceamento | Esperado ~97% classe 0 / ~3% classe 1 |

---

## 6. Roteiro do Vídeo (máx. 7 min)

| Tópico | Tempo sugerido |
|---|---|
| Objetivo do sistema + demonstração de funcionamento | 2 min |
| Como executar (requisitos + Jupyter) | 1 min |
| Como as tarefas foram organizadas (plano de projeto) | 1 min |
| Branches criadas e seus objetivos | 1 min |
| O que poderia melhorar no código | 1 min |
| Argumentação das escolhas técnicas | 1 min |

---

## 7. Critérios de Avaliação (resumo)

| Critério | Pontuação máxima |
|---|---|
| Gravação de vídeo | 2,0 |
| Uso do GitHub + README | 0,5 |
| EDA completa | 1,0 |
| Data Prep com justificativa | 1,0 |
| Feature Engineering | 1,0 |
| Divisão e Balanceamento | 1,0 |
| Escalonamento | 1,0 |
| Ajuste de hiperparâmetros | 1,0 |
| Avaliação e veredito final | 1,0 |
| **Total** | **10,0** |

---

_Última revisão: 2026-07-10_
