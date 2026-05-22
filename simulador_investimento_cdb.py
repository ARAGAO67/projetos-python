# 💰 Simulador de Investimento CDB 💰

taxa = 1.13 / 100

valor = float(input("💵 Digite o valor investido: "))
meses = int(input("📅 Digite a quantidade de meses: "))

resultado = valor * (1 + taxa) ** meses

print("🏦 Valor final: R$", round(resultado, 2))

# Nome: Lucas P Aragão