-- 1. INSERÇÕES VÁLIDAS (Fluxo Normal da Aplicação)

INSERT INTO ESPECIE (id_especie, nome_especie) VALUES (1, 'Cachorro');
INSERT INTO ESPECIE (id_especie, nome_especie) VALUES (2, 'Gato');
INSERT INTO ESPECIE (id_especie, nome_especie) VALUES (3, 'Ave');

INSERT INTO pet (nome_pet, id_especie, estado_triagem) VALUES ('Rex', 1, 'Aguardando');
INSERT INTO pet (nome_pet, id_especie, estado_triagem) VALUES ('Mia', 2, 'Em Consulta');

INSERT INTO historico_atendimento (id_pet, acao) VALUES (1, 'CADASTRAR');
INSERT INTO historico_atendimento (id_pet, acao) VALUES (1, 'CHAMAR');
INSERT INTO historico_atendimento (id_pet, acao) VALUES (2, 'CADASTRAR');

-- 2. TENTATIVAS DE INSERÇÃO INVÁLIDAS (Devem retornar ERRO)

INSERT INTO ESPECIE (id_especie, nome_especie) VALUES (4, NULL);
INSERT INTO ESPECIE (id_especie, nome_especie) VALUES (5, 'Cachorro');
INSERT INTO pet (nome_pet, id_especie, estado_triagem) VALUES ('Thor', 1, 'Finalizado');
INSERT INTO historico_atendimento (id_pet, acao) VALUES (1, 'CANCELAR');
INSERT INTO pet (nome_pet, id_especie, estado_triagem) VALUES ('Bidu', 99, 'Aguardando');