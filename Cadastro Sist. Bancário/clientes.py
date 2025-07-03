from json_utils import salvar_dados, carregar_dados

clientes = carregar_dados("clientes.json")

def cadastrar_cliente(nome, nascimento, cpf, endereco):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(" CPF já cadastrado.")
            return

    cliente = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    clientes.append(cliente)
    salvar_dados("clientes.json", clientes)
    print(" Cliente cadastrado com sucesso!")

def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None
