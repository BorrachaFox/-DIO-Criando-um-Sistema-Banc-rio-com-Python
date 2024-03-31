menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  option = input(menu + "\n>")

  if option == "1":
    print("Valor a ser depositado:")
    deposito = float(input("R$"))
    
    if deposito > 0:
      extrato += f'\nDeposito: R${deposito:.2f}'
      saldo += deposito
      continue
    
    print("Insira um valor valido")

  elif option == "2":
    print("Valor a ser sacado:")
    saque = abs(float(input("R$")))

    if saque > saldo :
      print("Saldo insulficiente")
    
    elif saque > limite: 
      print("Limite insulficiente")
    
    elif numero_saques >= LIMITE_SAQUES:
      print("Você atingiu o limite de saque diario")

    elif saque > 0:
      saldo -= saque
      extrato += f'\nSaque: R${saque:.2f}'
      numero_saques += 1
    else: 
      print("Insira um valor valido")

    
  elif option == "3":
    print("== Extrato do cliente ==")
    print("Nehuma movimentação foi realizada" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    
  
  elif option == "q":
    break

  else: 
    print("Operação invalida")
