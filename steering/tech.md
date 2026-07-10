# Tech — Decisões Técnicas Justificadas

## DT-01 · SMOTE sobre Random Under Sampling

**Decisão:** usar SMOTE para balancear a classe minoritária (falha = 1).  
**Justificativa:** O dataset tem ~3% de falhas. Random Under Sampling descartaria ~97% dos dados da maioria, perdendo informação real. O SMOTE gera amostras sintéticas interpoladas entre exemplos reais da minoria, preservando toda a informação da maioria.

---

## DT-02 · Mediana ou Média na Imputação

**Decisão:** tomada na Fase 2, com base na distribuição observada de cada coluna.  
**Regra:** distribuição simétrica (|skewness| < 1) → **Média** · assimétrica ou com outliers → **Mediana**  
**Por quê:** a média é deslocada por outliers; a mediana representa o valor central da ordenação e é insensível a extremos.

---

## DT-03 · StandardScaler apenas no KNN

**KNN:** usa distância euclidiana — variável com escala 1000× maior domina o cálculo.  
**Árvore:** usa thresholds binários (`rpm > 1500 ?`) — invariante à escala monotônica dos atributos.

---

## DT-04 · fit_transform no treino, transform no teste

`fit_transform` no teste aprenderia μ e σ do conjunto de teste, introduzindo informação do futuro. O X_test deve simular dados "novos" — usa os parâmetros aprendidos no treino.

---

## DT-05 · stratify=y no split

Com apenas ~3% de classe positiva, uma divisão aleatória pode gerar X_test com proporção distorcida. `stratify=y` garante a mesma proporção de classes em treino e teste.

---

## DT-06 · Excluir subtipos de falha do X

`falha_twf`, `falha_hdf`, `falha_pwf`, `falha_osf`, `falha_rnf` são sub-componentes da variável alvo. Incluí-los é **data leakage** — o modelo veria a resposta durante o treino.

---

## DT-07 · random_state=42 em todos os modelos

Garante reprodutibilidade — qualquer pessoa que clone o repositório e rode o notebook obtém exatamente os mesmos resultados numéricos.

---

## DT-08 · Exportação de métricas em JSON

JSON é o formato padrão de intercâmbio de dados em sistemas de produção. Demonstra conhecimento de deploy — o modelo produz artefatos consumíveis por outros sistemas. Usa apenas stdlib (`import json`).

---

_Última revisão: 2026-07-10_
