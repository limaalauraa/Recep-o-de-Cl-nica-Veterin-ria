CREATE TABLE ESPECIE (
    id_especie INT PRIMARY KEY,
    nome_especie VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE pet (
    id_pet INT AUTO_INCREMENT PRIMARY KEY,
    nome_pet VARCHAR(100) NOT NULL,
    id_especie INT NOT NULL,
    estado_triagem VARCHAR(20) DEFAULT 'Aguardando' NOT NULL,
    data_hora_recepcao TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (id_especie) REFERENCES ESPECIE(id_especie) ON DELETE RESTRICT,
    CHECK (estado_triagem IN ('Aguardando', 'Em Consulta'))
);

CREATE TABLE historico_atendimento (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    id_pet INT NOT NULL,
    acao VARCHAR(20) NOT NULL,
    data_hora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (id_pet) REFERENCES pet(id_pet) ON DELETE CASCADE,
    CHECK (acao IN ('CADASTRAR', 'CHAMAR'))
);
