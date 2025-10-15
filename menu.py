from agenda import inserir, consultar, remover, alterar, listar_contatos, salvar

def menu():
    while True:
        print("""
oooooooooooooooooooooooooooooooooooooooo
    
        - Agenda Telefônica -

        1- Inserir um novo contato 🆕
        2- Consultar um contato 🔎
        3- Remover um contato 🗑️
        4- Alterar um contato 📝
        5- Listar contatos 📃
        6- Salvar agenda ⬇️
        q - sair 👋

oooooooooooooooooooooooooooooooooooooooo
        """)

        opcao = input('O que deseja fazer? ')

        match opcao:
            case '1':
                inserir()
            case '2':
                consultar()
            case '3':
                remover()
            case '4':
                alterar()
            case '5':
                listar_contatos()
            case '6':
                salvar()
            case 'q':
                break
            case _:
                print('Opção inexistente! ❌\n')

