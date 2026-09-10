Dicionario:

pets_db = {}
  Cria o dicionário global vazio. Ele é a estrutura central onde a chave será sempre o `id_pet` 
  e o valor será outro dicionário com as informações do animal.

adicionar_pet(id_pet, nome_pet, especie)
  Cria um novo registro dentro do dicionário. A função recebe os dados e cria as quatro chaves obrigatórias: 
  `'id'`, `'nome_pet'`, `'especie'`, já definindo o `'status'` automaticamente como `"Aguardando"`.

colocar_em_consulta(id_pet)
  Acessa o pet diretamente pelo ID e muda automaticamente seu status para `"Em Consulta"`. 

voltar_para_espera(id_pet)
  Acessa o pet pelo ID e reverte seu status automaticamente para `"Aguardando"`. Caso o consultorio tenha colocado por engano.

encerrar_consulta(id_pet):
  Acessa o pet pelo ID e muda seu status para "Encerrado". Foi criada para finalizar o fluxo de atendimento do animal.

remover_pet(id_pet)
  Localiza o pet pelo ID e usa o comando `del` para excluir o registro inteiro do dicionário. Também serve para a função de 
  desfazer ações, apagando o cadastro caso o recepcionista tenha registrado o animal errado.

Pilha de Historico (pilha.py):

historico_veterinaria = []
  Cria a lista global que opera como Pilha (LIFO). Armazena as acoes do sistema como 
  tuplas imutaveis no formato ("ACAO", id_pet), como ("CADASTRAR", 101) ou ("CHAMAR", 101).

registrar_acao(acao, id_pet)
  Adiciona um novo registro de evento no topo da pilha de historico utilizando o metodo .append().

desfazer_ultima_acao()
  Remove a ultima acao do topo da pilha utilizando o metodo .pop() e executa o processo inverso:
  - Se for "CHAMAR": reverte o status do pet para "Aguardando" e chama a funcao reverter_chamada_na_fila(id_pet) para devolver o animal ao inicio da fila de espera.
  - Se for "CADASTRAR": chama reverter_cadastro_na_fila(id_pet) para tirar o ID da fila e apaga o registro do banco de dados utilizando a funcao remover_pet(id_pet).