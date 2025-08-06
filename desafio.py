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
    opcao = input(menu + "Escolha uma opção: ").lower()
    

    if opcao == "d":
       
            print("Depósito.")
            deposito = float(input("Digite o valor do depósito: "))
            
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            
            
    elif opcao == "s":
            
            print("saque.")
            saque = float(input("Digite o valor do saque: "))  
            if saque > limite:
                   print("Valor do saque excede o limite.")
            elif saque > saldo:
                   print("Saldo insuficiente para saque.")
            elif numero_saques > 3:
                     print("Número máximo de saques atingido.")
            else:
                        saldo -= saque
                        numero_saques += 1
                        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
                 
            

    elif opcao == "e":
         print("Extrato." + f"\nSaldo: R$ {saldo:.2f}") 

    elif opcao == "q":
      
        break

