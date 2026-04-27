#Exemplo de uso da variável sentinela#
while true:
    comando = input("Digite um comando-Para parar Digite `sair`")
if comando == "sair":
    break
print(f"Executando:{comando}")