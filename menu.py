# Inserir um novo contato
# Fazer consulta de um contato já cadastrado
# Remover um contato
# Alterar um contato

agenda = {}

def menu():
    while True:
        print("""
    ===================================
            
        - Agenda Telefônica -

        1- Inserir um novo contato
        2- Consultar um contato
        3- Remover um contato
        4- Alterar um contato
        q - sair

    ===================================
        """)

        opcao = input('O que deseja fazer? ')

        match opcao:
            case '1':
                inserir()
            case '2':
                consultar()
            case '3':
                pass
            case '4':
                alterar()
            case 'q':
                break
            case _:
                print('Opção inexistente!\n')

# nome, telefone, e-mail, contas do Twitter e Instagram
def inserir():
    try:
        qtd_contatos = int(input('Quantos contatos deseja adicionar? '))
        
        for i in range(qtd_contatos):
            print('\n')
            print(f'Adicionando contato {i + 1}\n')

            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o email do contato: ')
            twitter = input('Digite a conta do Twitter do contato: ')
            instagram = input('Digite a conta do Instagram do contato: ')

            agenda[nome] = {'telefone': telefone, 'email': email, 'twitter': twitter, 'instagram': instagram}
    except ValueError:
        print('ERROR: A quantidade precisa ser um número!')

def consultar():
    nome_consultado = input('Digite o nome do contato que deseja buscar: ')
    
    for contato in agenda: # Nesse caso seria possível adicionar detalhes no looping e .items()
        detalhes = agenda[contato]
        if contato == nome_consultado.lower(): 
            print(f"""
            Dados do Contato: {contato}
            Telefone: {detalhes['telefone']}
            Email: {detalhes['email']}
            Twitter: {detalhes['twitter']}
            Instagram: {detalhes['instagram']}
            """)
        else:
            print(f'Contato {nome_consultado} não foi encontrado!\n')

def alterar():
    nome_consultado = input('Qual contato deseja alterar? ')
    for contato in agenda:
        detalhes = agenda[contato]
        if contato == nome_consultado:
            dado_para_alterar = input('Qual dado deseja alterar? ')
            match dado_para_alterar.lower():
                case 'telefone':
                    novo_telefone = input('Digite o novo telefone: ')
                    detalhes['telefone'] = novo_telefone
                case 'email':
                    novo_email = input('Digite o novo email: ')
                    detalhes['email'] = novo_email
                case 'twitter':
                    novo_twitter = input('Digite o novo Twitter: ')
                    detalhes['twitter'] = novo_twitter
                case 'instagram':
                    novo_instagram = input('Digite o novo instagram: ')
                    detalhes['instagram'] = novo_instagram
                case _:
                    print('Dado inexistente!\n')
        else:
            print('Contato inexistente!\n')
