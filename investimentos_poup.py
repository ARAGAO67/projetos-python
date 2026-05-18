#Simulador de Investimento - Poupança--
deposito = float(input("Digite o valor do Aporte"))
taxa = float(input("Qual a taxa da Poupança em %?"))
meses = int(input("Quantos meses vai ivestir?"))
conversao = taxa/100
total = 0
for mes in range(1, meses +1):
   total = total + deposito
   total = total + (total * taxa)
print(f"Ao final do período, você terá:R${total:2f}")     