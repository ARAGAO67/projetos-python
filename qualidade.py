#Multiplas Funções--Exercício Controle de Qualidade--
def cabecalho():
    print("\n "+"="*30)
    print("SISTEMA DE QUALIDAE")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
       return "Aprovada"
    else:
       return "Reprovado"
cabecalho()
peso_item = float(input("Digite o Peso do Item em Gramas:"))
status = verificar_status(peso_item)
print(f"Resultado da Inspeção:{status}")
print("="*30)