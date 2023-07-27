saldo = 0
limite = 500
extrato = ""
quant_saque = 0
LIMIT_SAQUE = 3

menu = """

[1] Depostar
[2] Sacar
[3] Extrato
[4] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de deposito "))

        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou o valor informado é invalido")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = quant_saque >= LIMIT_SAQUE

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite diario. ")
        
        elif excedeu_saques:
            print("Operação falhou! foi utrapassado o limite de saques diario. ")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            quant_saque += 1

        else:
            print("Operação falhou o valor informado é invalido")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas as movimentaçãoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "4":
        break

    else:
        print("Operação invalida, por favor selecione a operação desejada. ")



