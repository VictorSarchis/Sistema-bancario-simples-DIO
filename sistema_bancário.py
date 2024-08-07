menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido. Digite um valor positivo para depósito.")

    elif opcao == "2":
        saque = float(input("Digite o valor que deseja sacar: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falou! Quantidade de saques excedeu o limite.")
        elif saque > limite:
            print("Operação falhou! Valor excede o limite para saque.")
        elif saque > saldo:
            print("Operação falhou! Saldo insuficiente para saque.")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
    
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print(f"{extrato}\nSaldo: R$ {saldo:.2f}\n")
        print("=============================")

    elif opcao == "4":
        break

    else:
        print("Operação invalida! Favor selecionar uma operação válida do menu.")