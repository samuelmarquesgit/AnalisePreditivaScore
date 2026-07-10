# Product — Visão e Posicionamento

## Visão

Construir um pipeline preditivo de classificação binária que permita a um parque fabril antecipar falhas mecânicas com base em leituras de sensores, reduzindo paradas inesperadas na linha de produção.

## Posicionamento

| Atributo | Valor |
|---|---|
| Usuário-alvo | Equipe de manutenção industrial / Gestores de produção |
| Problema resolvido | Paradas imprevistas por falhas mecânicas não detectadas antecipadamente |
| Solução | Modelo de ML que classifica risco de falha com base em sensores |
| Diferencial | Pipeline reprodutível, documentado e versionado — pronto para inspeção e auditoria |

## Critérios de Sucesso

| Critério | Meta |
|---|---|
| Acurácia no teste | > 85% no modelo campeão |
| Reprodutibilidade | Notebook roda do zero sem erros |
| Documentação | Todas as decisões técnicas justificadas em texto |
| Rastreabilidade | Histórico de commits claro e branches preservadas |

## Melhorias Futuras

1. Métricas mais ricas: F1-score e AUC-ROC para classes desbalanceadas
2. Mais algoritmos: Random Forest, XGBoost, LightGBM
3. Tuning automatizado: `GridSearchCV`
4. API REST via FastAPI para integração com sistemas SCADA
5. Monitoramento de Data Drift com `evidently`

---

_Última revisão: 2026-07-10_
