#lucas1: Formato do Nome do Filme
def formatar(nome):
    return nome.upper()
#aluno2:verificação de Acesso
def verificador(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não autorizado"
#Aluno3: Mensagem de retorno
def gerar_mensagem(status)
    if status == "Autorizado"
        return "Tenha uma ótima Sessão"
    else:
        return "Sinto Muito, Idade não autorizada"
#Aluno4: Itegrador do Projeto
nome_filme = input("Digite o nome do Filme:")
idade_filme = int(input("Digite sua Idade:"))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\n Filme:{filme}")
print(f"status:{status_final}")
print(f"aviso:{mensagem}")
    
    