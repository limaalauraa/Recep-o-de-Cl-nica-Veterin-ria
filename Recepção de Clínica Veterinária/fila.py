fila_espera = []

def entrar_na_fila(id_pet):
    fila_espera.append(id_pet)
    print(f"Pet {id_pet} entrou na fila de espera.")

def chamar_proximo_pet():
    if not fila_espera:
        print("Não tem pets na fila de espera.")
        return None
    else:
        proximo_pet = fila_espera.pop(0)
        print(f"Pet {proximo_pet} foi chamado.")
        return proximo_pet

def reverter_chamada_na_fila(id_pet):
    fila_espera.insert(0, id_pet)

def reverter_cadastro_na_fila(id_pet):
    if id_pet in fila_espera:
        fila_espera.remove(id_pet)
