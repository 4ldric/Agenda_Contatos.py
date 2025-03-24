
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
        print(f' Nome: {nome_contato}\n Telefone: {telefone_contato}\n Email: {email_contato}')
    else:
        print("informe digito correto!!")


def editar_contato(contatos,indice_contato, novo_nome,novo_numero, novo_email):
    indice_revisado = indice_contato - 1

    print("Contato Atualizado")

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
        
    elif comando == 7:
        break