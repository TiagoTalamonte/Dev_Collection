from clientes import cadastrar_cliente, buscar_cliente_por_cpf
import contas
import banco

conta_ativa = None  
menu = """
========= MENU =========
[0] Selecionar Conta
[1] Depositar
[2] Sacar
[3] Ver Extrato
[4] Cadastrar Cliente
[5] Buscar Cliente por CPF
[6] Criar Nova Conta
[7] Listar Contas
[8] Sair
========================
Escolha uma opção: """

while True:
    opcao = input(menu).lower()

    if opcao == "0":
        try:
            numero = int(input("Informe o número da conta: "))
            conta = contas.buscar_conta_por_numero(numero)
            if conta:
                conta_ativa = conta
                print(f" Conta {numero} selecionada com sucesso.")
            else:
                print(" Conta não encontrada.")
        except ValueError:
            print(" Número inválido.")

    elif opcao == "1":
        if not conta_ativa:
            print(" Nenhuma conta selecionada.")
            continue
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            banco.depositar(conta_ativa, valor)
        except ValueError:
            print(" Valor inválido.")

    elif opcao == "2":
        if not conta_ativa:
            print(" Nenhuma conta selecionada.")
            continue
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            banco.sacar(conta_ativa, valor)
        except ValueError:
            print(" Valor inválido.")

    elif opcao == "3":
        if not conta_ativa:
            print(" Nenhuma conta selecionada.")
            continue
        banco.mostrar_extrato(conta_ativa)

    elif opcao == "4":
        nome = input("Nome: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (Rua, número - Bairro - Cidade/UF): ")
        cadastrar_cliente(nome, nascimento, cpf, endereco)

    elif opcao == "5":
        cpf = input("Digite o CPF a buscar: ")
        cliente = buscar_cliente_por_cpf(cpf)
        if cliente:
            print(" Cliente encontrado:")
            print(cliente)
        else:
            print(" Cliente não encontrado.")

    elif opcao == "6":
        cpf = input("Informe o CPF do cliente: ")
        cliente = buscar_cliente_por_cpf(cpf)
        if cliente:
            contas.criar_conta(cpf)
        else:
            print(" Cliente não encontrado. Cadastre o cliente antes de criar a conta.")

    elif opcao == "7":
        contas.listar_contas()

    elif opcao == "8":
        print(" Encerrando o sistema. Até logo!")
        break

    else:
        print(" Opção inválida. Tente novamente.")
