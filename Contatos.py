
def adicionar_contato(nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(contatos)

contatos = []

while True:
    print("=== Agenda de Contatos ===")

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
        telefone = input("Numero do contato: ")
        email = input("Email do contato: ")
        adicionar_contato(nome, telefone, email)
    elif comando == 2:
        print(contatos)
    elif comando == 7:
        break