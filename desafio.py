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
            if saque != numero_saques:
                  
                  print("Número de saques excedido.")
            elif saque > limite:
                  print("Valor do saque excede o limite.")

                         
    
    elif opcao == "e":
       
         print("Extrato." + f"\nSaldo: R$ {saldo:.2f}") 

    elif opcao == "q":
      
        break

