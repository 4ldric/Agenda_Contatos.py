
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
    print("=+=+=+= Lista de contatos ")
    for indice,contato in enumerate(contatos, start=1):
        favorito = "☆" if contato["favoritos"] else " "
        nome_contato = contato["nome"]
        print(f'{indice}. [{favorito} ] {nome_contato}')

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
            print("Nome Atualizado!!\n")
        elif editar == 2:
            novo_telefone = int(input("Digite o telefone atualizado: "))
            contatos[indice_revisado]["telefone"] = novo_telefone
            print("Telefone Atualizado!!\n")
        elif editar == 3:
            novo_email = input("Digite o email atualizado: ")
            contatos[indice_revisado]["email"] = novo_email
            print("Email Atualizado!!\n")
        elif editar == 0:
            editor -= 1
            print("Retornando ao menu...")

def favoritar_contato(contatos, indice_contato):
    indice_revisado = indice_contato - 1
    opcao = contatos[indice_revisado]["favoritos"]
    if indice_revisado >= 0 and indice_revisado < len(contatos):
        if opcao is False:
            contatos[indice_revisado]["favoritos"] = True
            print("Contato Favoritado!!\n")
        else:
            contatos[indice_revisado]["favoritos"] = False
            print("Contato Removido dos favoritos!!\n")
    print("Retornando ao menu!!\n")

def ver_favoritos():
    print("=+=+=+= Contatos favoritos =+=+=+=")
    if contatos == []:
        print("Nenhum contato favoritado, retornando ao menu..")
    else:
        for indice, contato in enumerate(contatos, start=1):
            if contato["favoritos"] is True:
                nome_contato = contato["nome"]
                favorito = "☆" 
                print(f' {indice}. [{favorito} ] {nome_contato}')
            elif contato["favoritos"] is False:
                continue


contatos = []

while True:
    print("\n=== Agenda de Contatos ===")

    print("""
    [1] Adicionar Contato
    [2] Ver contatos
    [3] Editar contato
    [4] Adicionar ou remover contato dos favoritos
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
    elif comando == 4:
        ver_contatos()
        indice_contato = int(input("digite Qual contato deseja favoritar/remover favorito: "))
        favoritar_contato(contatos, indice_contato)
    elif comando == 5:
        ver_favoritos()
    elif comando == 7:
        break
    else:
        print("informe apenas digitos disponiveis..")