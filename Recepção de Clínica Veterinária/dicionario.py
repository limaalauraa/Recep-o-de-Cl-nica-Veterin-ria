from lista import validar_especie, adicionar_especie

pets_db = {}

def adicionar_pet(id_pet, nome_pet, especie):
    if not validar_especie(especie):
        print(f"\n[ERRO] Espécie '{especie}' não é atendida por esta clínica.")
        return False

    pets_db[id_pet] = {
        'id': id_pet,
        'nome_pet': nome_pet,
        'especie': especie,
        'status': "Aguardando"
    }
    return True

def colocar_em_consulta(id_pet):
    pets_db[id_pet]['status'] = "Em Consulta"

def voltar_para_espera(id_pet):
    pets_db[id_pet]['status'] = "Aguardando"

def encerrar_consulta(id_pet):
    pets_db[id_pet]['status'] = "Encerrado"

def remover_pet(id_pet):
    del pets_db[id_pet]


if __name__ == "__main__":
    print("0. Cadastrando espécies atendidas para o teste...")
    adicionar_especie("Cachorro")
    adicionar_especie("Gato")
    print("-" * 40)

    print("1. Dicionário inicial (vazio):")
    print(pets_db)
    print("-" * 40)

    print("2. Adicionando dois pets...")
    adicionar_pet(101, "Rex", "Cachorro")
    adicionar_pet(102, "Mimi", "Gato")
    print(pets_db)
    print("-" * 40)

    print("3. Colocando o Rex (101) em consulta...")
    colocar_em_consulta(101)
    print(pets_db[101]) 
    print("-" * 40)

    print("4. Voltando o Rex (101) para espera (simulando um erro de chamada)...")
    voltar_para_espera(101)
    print(pets_db[101])
    print("-" * 40)

    print("5. Removendo a Mimi (102) (simulando um cadastro errado)...")
    remover_pet(102)
    print("Dicionário final:")
    print(pets_db)
