# Recep-o-de-Cl-nica-Veterin-riaDicionario:

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

# Recepção-de-Clínica-Veterinária-Fila:

fila_espera = []
  Cria a lista global vazia. Ela é a estrutura central da fila de espera que armazena os IDs dos pets por ordem de chegada.

entrar_na_fila(id_pet)
  Adiciona o ID do pet ao final da lista usando o comando `.append()`, seguindo a política FIFO (First In, First Out).

chamar_proximo_pet()
  Retira e retorna o primeiro ID da fila utilizando o comando `.pop(0)` para enviar o pet ao atendimento. Caso a fila esteja vazia, exibe uma mensagem de aviso.

reverter_chamada_na_fila(id_pet)
  Devolve o pet para a primeira posição da fila usando o comando `.insert(0, id_pet)`. Serve para a função de desfazer ações caso o pet tenha sido chamado por engano.

reverter_cadastro_na_fila(id_pet)
  Localiza e remove o ID do pet da lista com o comando `.remove()` caso o cadastro do animal seja cancelado no sistema.
