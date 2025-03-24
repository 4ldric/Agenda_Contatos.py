
def adicionar_contato(nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favoritos": False
    }
    contatos.append(contato)
    print("Contato adicionado!!")

def ver_contatos():
    print("Lista de contatos")
    for indice,contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favoritos"] else " "
        nome_contato = contato["nome"]
        print(f'{indice}. [{favorito}] {nome_contato}')

def detalhes_contato(indice_contato):
    indice_revisado = indice_contato - 1
    if indice_revisado >= 0:
        print(f"\n   Contato {indice_contato}    ")
        nome_contato = contatos[indice_revisado]["nome"]
        telefone_contato = contatos[indice_revisado]["telefone"]
        email_contato = contatos[indice_revisado]["email"]
        print(f' [1] Nome: {nome_contato}\n [2] Telefone: {telefone_contato}\n [3] Email: {email_contato}')
    elif indice_contato == 0:
        print("Retornando ao menu...")
    else:
        print("informe digito correto!!")


def editar_contato(indice_contato):
    indice_revisado = indice_contato - 1
    editor = 1
    detalhes_contato(indice_contato)
    while editor > 0:
        editar = int(input("Digite o que deseja atualizar ou digite 0 para retornar ao menu: "))
        if editar == 1:
            novo_nome = input("Digite o nome atualizado: ")
            contatos[indice_revisado]["nome"] = novo_nome
            print("Nome Atualizado!!")
        elif editar == 2:
            novo_telefone = int(input("Digite o telefone atualizado: "))
            contatos[indice_revisado]["telefone"] = novo_telefone
            print("Telefone Atualizado!!")
        elif editar == 3:
            novo_email = input("Digite o email atualizado: ")
            contatos[indice_revisado]["email"] = novo_email
        elif editar == 0:
            editor -= 1
            print("Retornando ao menu...")

contatos = []

while True:
    print("\n=== Agenda de Contatos ===")

    print("""
    [1] Adicionar Contato
    [2] Ver contatos
    [3] Editar contato
    [4] Favoritar contato
    [5] Ver favoritos
    [6] Remover contato
    [7] Sair
    """)

    comando = int(input("Digite o comando desejado: "))

    if comando == 1:
        nome = input("Nome do contato: ")
        telefone = int(input("Numero do contato: "))
        email = input("Email do contato: ")
        adicionar_contato(nome, telefone, email)
    elif comando == 2:
        ver_contatos()
        indice_contato = int(input("\ndeseja ver o contato? digite o numero ou 0 para sair: "))
        detalhes_contato(indice_contato)
    elif comando == 3:
        ver_contatos()
        indice_contato = int(input("Informe o contato a ser editado: "))
        editar_contato(indice_contato)
        
    elif comando == 7:
        break