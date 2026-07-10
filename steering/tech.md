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

## DT-09 · Auditoria e modelos avançados como extensão exploratória, não substituição (exploratório)

**Decisão:** a auditoria do modelo (Model Card) e as Fases 8-10 (Random Forest, XGBoost, LightGBM) foram adicionadas como seções à parte, depois da Fase 7, em vez de substituir a comparação KNN vs Árvore.  
**Por quê:** o enunciado exige especificamente a comparação entre KNN e Árvore de Decisão (Seção 7 do `docs/PRD.md`). Misturar os modelos exploratórios no veredito oficial da Fase 7 arriscaria descumprir esse requisito. Mantendo-os separados, a extensão soma valor (auditoria mais rigorosa, benchmark contra modelos mais robustos) sem colocar em risco a nota da entrega obrigatória.

---

## DT-10 · Recall como métrica-guia da auditoria, não a acurácia (exploratório)

**Decisão:** a auditoria prioriza o **recall da classe Falha (1)**, não a acurácia, para avaliar risco.  
**Por quê:** com ~97% dos exemplos na classe "Normal", a acurácia isolada é enganosa — um classificador trivial que sempre prevê "Normal" teria ~97% de acurácia sem detectar nenhuma falha. Em manutenção preditiva, um falso negativo (falha não detectada) tem custo maior que um falso positivo (manutenção desnecessária), o que torna o recall a métrica mais relevante para avaliar o risco real do modelo — mesmo que o critério de seleção oficial da Fase 7 continue sendo a acurácia, por exigência do enunciado.

---

_Última revisão: 2026-07-10_
