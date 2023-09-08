saldo = 0.0
depositos = []
saques = []

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
    else:
        print("O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo
    if valor <= 500.0 and valor <= saldo:
        saldo -= valor
        saques.append(valor)
    else:
        print("Saque não permitido. Verifique o valor ou saldo disponível.")

def extrato():
    print("### Extrato ###")
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        for i, valor in enumerate(depositos, 1):
            print(f"Depósito {i}: RS {valor:.2f}")
        for i, valor in enumerate(saques, 1):
            print(f"Saque {i}: RS {valor:.2f}")
    print(f"Saldo atual: RS {saldo:.2f}")

while True:
    print("\nEscolha uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
