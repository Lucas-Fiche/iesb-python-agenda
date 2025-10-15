# Inserir um novo contato
# Fazer consulta de um contato já cadastrado
# Remover um contato
# Alterar um contato
from tabulate import tabulate

agenda = {}

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

            agenda[nome.lower()] = {'nome': nome, 'telefone': telefone, 'email': email, 'twitter': twitter, 'instagram': instagram}
            
    except ValueError:
        print('❌ ERROR: A quantidade precisa ser um número!')

def consultar():
    nome_consultado = input('Digite o nome do contato que deseja buscar: ')
    encontrado = False

    for contato in agenda: # Nesse caso seria possível adicionar detalhes no looping e .items()
        detalhes = agenda[contato]
        
        if contato.lower() == nome_consultado.lower(): 
            print(f"""
***************************************
🧑 Dados do Contato: {detalhes['nome']} 
📞 Telefone: {detalhes['telefone']} 
✉️ Email: {detalhes['email']} 
🐦 Twitter: {detalhes['twitter']} 
📷 Instagram: {detalhes['instagram']} 
***************************************
            """)
            encontrado = True
            break
        
    if not encontrado:
        print('==============================================')
        print(f'O contato {nome_consultado} não existe! ❌\n')
        print('==============================================')
            
def remover():
    nome_consultado = input('Qual contato deseja remover? ')
    
    if nome_consultado.lower() in agenda:
        agenda.pop(nome_consultado)
        print('================================================')
        print(f'Contato {nome_consultado} removido com sucesso! ✅')
        print('==============================================\n')
    else:
        print('============================================')
        print(f'O contato {nome_consultado} não existe! ❌')
        print('============================================\n')        


def alterar():
    nome_consultado = input('Qual contato deseja alterar? ')
    encontrado = False
    for contato in agenda:
        detalhes = agenda[contato]
        if contato.lower() == nome_consultado.lower():
            encontrado = True
            dado_para_alterar = input('Qual dado deseja alterar? ')
            match dado_para_alterar.lower():
                case 'nome':
                    novo_nome = input('Digite o novo nome: ')
                    detalhes['nome'] = novo_nome
                    print('===========================')
                    print(f'Nome alterado com sucesso! ✅')
                    print('===========================\n')
                case 'telefone':
                    novo_telefone = input('Digite o novo telefone: ')
                    detalhes['telefone'] = novo_telefone
                    print('===============================')
                    print(f'Telefone alterado com sucesso! ✅')
                    print('===============================\n')
                case 'email':
                    novo_email = input('Digite o novo email: ')
                    detalhes['email'] = novo_email
                    print('===============================')
                    print(f'Email alterado com sucesso! ✅')
                    print('===============================\n')
                case 'twitter':
                    novo_twitter = input('Digite o novo Twitter: ')
                    detalhes['twitter'] = novo_twitter
                    print('===============================')
                    print(f'Twitter alterado com sucesso! ✅')
                    print('===============================\n')
                case 'instagram':
                    novo_instagram = input('Digite o novo instagram: ')
                    detalhes['instagram'] = novo_instagram
                    print('===============================')
                    print(f'Instagram alterado com sucesso! ✅')
                    print('===============================\n')
                case _:
                    print('=====================')
                    print('Dado inexistente! ❌')
                    print('=====================\n')
        
    if not encontrado:
        print('============================================')
        print(f'Contato {nome_consultado} inexistente! ❌\n')
        print('============================================')

def listar_contatos():
    cabecalho = ["Nº", "Nome", "Telefone", "Email", "Twitter", "Instagram"]
    dados = []
    i = 1
    for contato in agenda:
        detalhes = agenda[contato]
        contato_atual = [
            i,
            detalhes['nome'],
            detalhes['telefone'],
            detalhes['email'],
            detalhes['twitter'],
            detalhes['instagram']
        ]
        i = i + 1
        print(i)
        dados.append(contato_atual)

    print(tabulate(dados, headers=cabecalho))

def carregar_agenda():
    try:
        with open('agenda.txt', 'r') as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                dados = linha_limpa.split(',')

                nome = dados[0]
                telefone = dados[1]
                email = dados[2]
                twitter = dados[3]
                instagram = dados[4]

                agenda[nome.lower()] = {
                    'nome': nome,
                    'telefone': telefone,
                    'email': email,
                    'twitter': twitter,
                    'instagram': instagram
                }

                print("\n✅ - Arquivo 'agenda.txt' carregado com sucesso!\n")
    except FileNotFoundError:
        print("ℹ️ - Arquivo 'agenda.txt' não encontrado. Começando com uma agenda vazia.")
    except Exception as e:
        print(f"❌ - Ocorreu um erro ao carregar a agenda: {e}")


def salvar():
    with open('agenda.txt', 'w', encoding='utf-8') as arquivo:
        for contato in agenda:
            detalhes = agenda[contato]
            linha = f'{detalhes['nome']}, {detalhes['telefone']}, {detalhes['email']}, {detalhes['twitter']}, {detalhes['instagram']}\n'
            arquivo.write(linha)

    print('===================================================')
    print('✅ Agenda salva com sucesso no arquivo agenda.txt!')
    print('=================================================\n')