from json_utils import salvar_dados, carregar_dados

contas = carregar_dados("contas.json") or []
contador_contas = max([c["numero"] for c in contas], default=0) + 1

def criar_conta(cpf):
    global contador_contas

    conta = {
        "numero": contador_contas,
        "cpf": cpf,
        "saldo": 0.0,
        "extrato": "",
        "limite_saques": 3
    }

    contas.append(conta)
    salvar_dados("contas.json", contas)
    print(f" Conta Nº {contador_contas} criada para CPF {cpf}")
    contador_contas += 1

def listar_contas():
    if not contas:
        print(" Nenhuma conta encontrada.")
        return

    print("\n CONTAS REGISTRADAS:")
    for conta in contas:
        print(f" Conta Nº: {conta['numero']} | CPF: {conta['cpf']}")

def buscar_conta_por_numero(numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None

def salvar_todas_contas():
    salvar_dados("contas.json", contas)
