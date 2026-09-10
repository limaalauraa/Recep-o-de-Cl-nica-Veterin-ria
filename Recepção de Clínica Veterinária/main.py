from lista import especies_atendidas, adicionar_especie
from dicionario import pets_db, adicionar_pet, colocar_em_consulta
from fila import fila_espera, entrar_na_fila, chamar_proximo_pet
from pilha import historico_veterinaria, registrar_acao, desfazer_ultima_acao


def cadastrar_pet(id_pet, nome_pet, especie):
    
    sucesso = adicionar_pet(id_pet, nome_pet, especie)
    if not sucesso:
        return

    entrar_na_fila(id_pet)
    registrar_acao("CADASTRAR", id_pet)
    print(f"[OK] Pet '{nome_pet}' (ID {id_pet}) cadastrado e adicionado à fila de espera.")


def chamar_proximo():
    id_pet = chamar_proximo_pet()
    if id_pet is not None:
        colocar_em_consulta(id_pet)
        registrar_acao("CHAMAR", id_pet)


def exibir_painel():
    print("\n" + "=" * 50)
    print("PAINEL DA CLÍNICA VETERINÁRIA")
    print("=" * 50)
    print(f"Fila de espera.........: {fila_espera}")
    print(f"Base de dados (pets_db).: {pets_db}")
    print(f"Histórico de ações......: {historico_veterinaria}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    print("1. Cadastrando as espécies atendidas pela clínica...")
    adicionar_especie("Cachorro")
    adicionar_especie("Gato")
    adicionar_especie("Ave")
    print(f"Espécies atendidas: {especies_atendidas}")

    exibir_painel()

    print("2. Cadastrando pets na recepção...")
    cadastrar_pet(101, "Rex", "Cachorro")
    cadastrar_pet(102, "Mimi", "Gato")
    cadastrar_pet(103, "Piu-Piu", "Réptil") 

    exibir_painel()

    print("3. Chamando o próximo pet da fila (FIFO)...")
    chamar_proximo()

    exibir_painel()

    print("4. Desfazendo a última ação (a chamada do pet)...")
    desfazer_ultima_acao(fila_espera)

    exibir_painel()

    print("5. Liberando a espécie 'Réptil' e cadastrando o pet 103 corretamente...")
    adicionar_especie("Réptil")
    cadastrar_pet(103, "Piu-Piu", "Réptil")

    exibir_painel()

    print("6. Desfazendo a última ação (o cadastro do pet 103)...")
    desfazer_ultima_acao(fila_espera)

    exibir_painel()
