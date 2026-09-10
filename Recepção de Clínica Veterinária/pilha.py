from dicionario import pets_db, voltar_para_espera, remover_pet
from fila import reverter_chamada_na_fila, reverter_cadastro_na_fila

historico_veterinaria = []

def registrar_acao(acao, id_pet):
    historico_veterinaria.append((acao, id_pet))

def desfazer_ultima_acao(fila_espera):
    if not historico_veterinaria:
        print("\n[AVISO] Não há nenhuma ação no histórico para desfazer.")
        return

    acao, id_pet = historico_veterinaria.pop()

    if acao == "CHAMAR":
        if id_pet in pets_db:
            voltar_para_espera(id_pet)
        reverter_cadastro_na_fila(id_pet)
        fila_espera.insert(0, id_pet)
        print(f"\n[DESFAZER] Ação 'CHAMAR' desfeita! Pet ID {id_pet} retornou ao início da fila.")

    elif acao == "CADASTRAR":
        reverter_cadastro_na_fila(id_pet)
        if id_pet in pets_db:
            remover_pet(id_pet)
        print(f"\n[ERRO] Ação 'CADASTRAR' desfieita! Pet ID {id_pet} removido do sistema.")

    else:
        print(f"\n[ERRO] Ação '{acao}' não reconhecida pelo histórico.")