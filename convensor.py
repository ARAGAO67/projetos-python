#Ferramenta de Conversão Dólar x Real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor DólarxReal")
preco = float(input("Digite o preço do porduto:"))
resultado = converter(preco)
print(f"O valor em Reais é:{resultado:.2f}")