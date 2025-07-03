import contas

def depositar(conta, valor):
    if valor <= 0:
        print(" Valor inválido para depósito.")
        return

    conta["saldo"] += valor
    conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    print(" Depósito realizado com sucesso.")
    contas.salvar_todas_contas()


def sacar(conta, valor):
    if valor > conta["saldo"]:
        print(" Saldo insuficiente.")
    elif conta["limite_saques"] <= 0:
        print(" Limite de saques atingido.")
    elif valor <= 0:
        print(" Valor inválido para saque.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["limite_saques"] -= 1
        print(" Saque realizado com sucesso.")
        contas.salvar_todas_contas()


def mostrar_extrato(conta):
    print("\n EXTRATO")
    print(conta["extrato"] if conta["extrato"] else "Sem movimentações.")
    print(f"Saldo atual: R$ {float(conta['saldo']):.2f}")
    print("=" * 20)
