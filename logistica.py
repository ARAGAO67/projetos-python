# --Calculadora de Frete--

def calcular_frete(peso):
    # 📦 Verifica o peso da carga
    if peso <= 20:
        custo = peso * 10
        print("✅ Carga leve!")
    else:
        custo = peso * 15
        print("⚠️ Carga pesada!")

    return custo


# 📝 Entrada de dados
peso_carga = float(input("Digite o peso da carga em kg ⚖️: "))

# 💰 Cálculo do frete
valor_frete = calcular_frete(peso_carga)

# 📢 Resultado final
print(f"🚚 O valor final do frete é: R$ {valor_frete:.2f}")