-- DDL Schema — PredictMaint
-- Uso futuro: persistir o dataset e as métricas em banco de dados relacional

CREATE TABLE IF NOT EXISTS leituras_sensor (
    udi                     INTEGER PRIMARY KEY,
    id_produto              VARCHAR(10) NOT NULL,
    tipo                    CHAR(1) NOT NULL CHECK (tipo IN ('L', 'M', 'H')),
    temperatura_ar_k        NUMERIC(6, 2),
    temperatura_processo_k  NUMERIC(6, 2),
    velocidade_rotacao_rpm  NUMERIC(8, 2),
    torque_nm               NUMERIC(6, 2),
    desgaste_ferramenta_min INTEGER NOT NULL,
    falha_maquina           SMALLINT NOT NULL CHECK (falha_maquina IN (0, 1)),
    falha_twf               SMALLINT DEFAULT 0,
    falha_hdf               SMALLINT DEFAULT 0,
    falha_pwf               SMALLINT DEFAULT 0,
    falha_osf               SMALLINT DEFAULT 0,
    falha_rnf               SMALLINT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS metricas_modelo (
    id                  SERIAL PRIMARY KEY,
    data_execucao       TIMESTAMP DEFAULT NOW(),
    algoritmo           VARCHAR(50) NOT NULL,
    hiperparametro      VARCHAR(50),
    acuracia_treino     NUMERIC(5, 4),
    acuracia_teste      NUMERIC(5, 4),
    modelo_selecionado  BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS features_derivadas (
    udi      INTEGER REFERENCES leituras_sensor(udi),
    potencia NUMERIC(12, 4)
);

-- Última revisão: 2026-07-10
