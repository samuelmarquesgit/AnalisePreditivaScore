# Requisitos — PredictMaint

## Requisitos Funcionais (RF)

| ID | Requisito | Critério de Aceite | Status |
|---|---|---|---|
| RF01 | Carregar e exibir dimensões do dataset | `df.shape` retorna (n_linhas, 14) sem erro | ✅ |
| RF02 | Exibir tipos de dados e resumo estatístico | `dtypes` e `describe()` executam sem erro | ✅ |
| RF03 | Plotar mínimo 3 gráficos analíticos na EDA | Histograma + barras + heatmap presentes | ✅ |
| RF04 | Remover linhas duplicadas | `duplicated().sum() == 0` após limpeza | ✅ |
| RF05 | Imputar valores ausentes com média ou mediana | Nenhuma coluna preditora com NaN após imputação | ✅ |
| RF06 | Gerar boxplots das variáveis explicativas | Boxplot de cada variável contínua presente | ✅ |
| RF07 | Criar coluna `potencia` | `'potencia' in df.columns` e sem NaN | ✅ |
| RF08 | Separar X e y corretamente | X sem colunas de subtipo de falha e sem `falha_maquina` | ✅ |
| RF09 | Dividir dados 80/20 com estratificação | `test_size=0.2`, `stratify=y` no split | ✅ |
| RF10 | Aplicar SMOTE exclusivamente no treino | X_test não passa pelo SMOTE | ✅ |
| RF11 | Aplicar StandardScaler corretamente no KNN | `fit_transform` no treino, `transform` no teste | ✅ |
| RF12 | Manter dados da Árvore sem escalonamento | Árvore treinada com X original | ✅ |
| RF13 | Treinar KNN com K = 3, 5, 7 | Acurácia de treino e teste registrada para cada K | ✅ |
| RF14 | Treinar Árvore com max_depth = 3, 5, None | Acurácia de treino e teste registrada para cada depth | ✅ |
| RF15 | Identificar overfitting em texto | Célula markdown apontando onde gap treino > teste | ✅ |
| RF16 | Calcular e exibir acurácia final dos dois modelos | `accuracy_score` para melhor KNN e melhor Árvore | ✅ |
| RF17 | Escrever veredito final fundamentado | Conclusão com comparação numérica e modelo recomendado | ✅ |

## Requisitos Não-Funcionais (RNF)

| ID | Requisito | Critério de Aceite | Status |
|---|---|---|---|
| RNF01 | Reprodutibilidade | `Restart & Run All` executa sem erros em qualquer máquina | ⬜ |
| RNF02 | Caminhos relativos | Nenhum caminho absoluto no notebook | ✅ |
| RNF03 | Documentação de decisões | Cada fase possui célula Markdown de justificativa | ⬜ |
| RNF04 | Rastreabilidade Git | Uma branch por fase com commits descritivos | ⬜ |
| RNF05 | Dependências declaradas | `requirements.txt` com versões fixas presente no repo | ⬜ |
| RNF06 | Repositório público | GitHub em modo público — avaliador consegue clonar | ⬜ |
| RNF07 | Código autoral | Todos os blocos integral gerado por IA (Seção 8) | ✅ |

---

_Última revisão: 2026-07-10_
