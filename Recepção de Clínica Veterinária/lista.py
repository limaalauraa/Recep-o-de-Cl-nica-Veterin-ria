especies_atendidas = []


def adicionar_especie(nome_especie):
    if nome_especie not in especies_atendidas:
        especies_atendidas.append(nome_especie)
        print(f"Espécie '{nome_especie}' adicionada à lista de espécies atendidas.")
    else:
        print(f"Espécie '{nome_especie}' já está cadastrada (não são permitidas duplicatas).")


def validar_especie(nome_especie):
    return nome_especie in especies_atendidas


if __name__ == "__main__":
    print("1. Lista de espécies atendidas (vazia):")
    print(especies_atendidas)
    print("-" * 40)

    print("2. Adicionando espécies...")
    adicionar_especie("Cachorro")
    adicionar_especie("Gato")
    adicionar_especie("Ave")
    print(especies_atendidas)
    print("-" * 40)

    print("3. Tentando adicionar uma espécie duplicada (Gato)...")
    adicionar_especie("Gato")
    print(especies_atendidas)
    print("-" * 40)

    print("4. Validando espécies...")
    print(f"'Cachorro' é atendida? {validar_especie('Cachorro')}")
    print(f"'Réptil' é atendida? {validar_especie('Réptil')}")
