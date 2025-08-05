menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
  
 =>   """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
       
            print("Depósito.")

    elif opcao == "s":
       
            print("saque.")

    elif opcao == "e":
       
        print("Extrato.")

    elif opcao == "q":
      
        break

    