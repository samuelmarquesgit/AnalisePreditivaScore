# Product — Visão e Posicionamento

## Visão

Construir um pipeline preditivo de classificação binária que permita a um parque fabril antecipar falhas mecânicas com base em leituras de sensores, reduzindo paradas inesperadas na linha de produção.

## Posicionamento

| Atributo | Valor |
|---|---|
| Usuário-alvo | Equipe de manutenção industrial / Gestores de produção |
| Problema resolvido | Paradas imprevistas por falhas mecânicas não detectadas antecipadamente |
| Solução | Modelo de ML que classifica risco de falha com base em sensores |
| Diferencial | Pipeline reprodutível, documentado e versionado — pronto para inspeção e auditoria (ver `docs/auditoria/model_card.md`) |

## Critérios de Sucesso

| Critério | Meta |
|---|---|
| Acurácia no teste | > 85% no modelo campeão |
| Reprodutibilidade | Notebook roda do zero sem erros |
| Documentação | Todas as decisões técnicas justificadas em texto |
| Rastreabilidade | Histórico de commits claro e branches preservadas |

## Extensão Exploratória (concluída, não obrigatória)

- Auditoria do modelo (Model Card): matriz de confusão, precisão/recall/F1, desempenho por tipo de máquina — `docs/auditoria/model_card.md`
- Comparação ampliada com Random Forest, XGBoost e LightGBM (Fases 8-10 do notebook)

## Melhorias Futuras

1. AUC-ROC para classes desbalanceadas
2. Tuning automatizado: `GridSearchCV` (incluindo os modelos da extensão exploratória)
3. API REST via FastAPI para integração com sistemas SCADA
4. Monitoramento de Data Drift com `evidently`

---

_Última revisão: 2026-07-10_
