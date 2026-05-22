# 💰 Simulador de Investimento CDB 💰

# 📈 Taxa mensal atual aproximada do CDB/CDI
taxa_mensal = 1.13 / 100

print("💵 ===== SIMULADOR DE INVESTIMENTO CDB ===== 💵")

# 📝 Entrada de dados
valor_inicial = float(input("💲 Digite o valor do investimento: R$ "))
meses = int(input("📅 Digite a quantidade de meses: "))

# 🧮 Cálculo dos juros compostos
valor_final = valor_inicial * (1 + taxa_mensal) ** meses

# 📊 Resultado
print("\n📈 ===== RESULTADO ===== 📈")
print(f"💰 Valor investido: R$ {valor_inicial:.2f}")
print(f"⏳ Tempo investido: {meses} meses")
print(f"📌 Taxa mensal: {taxa_mensal * 100:.2f}%")
print(f"🏦 Valor final: R$ {valor_final:.2f}")

#Nome: Lucas P Aragão