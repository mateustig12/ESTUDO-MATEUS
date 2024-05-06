import os
restaurantes = [{'nome':'Mateus', 'categoria':'italiana', 'ativo':False},
                {'nome':'Ramos', 'categoria':'japones', 'ativo':True},
                {'nome':'Brhennda', 'categoria':'australiana', 'ativo':False},]

def exibir_nome_programa():
    print('Sabor express\n')

def exibir_opções():
    print('1. Cadastro de novo restaurante')
    print('2. Listar restaurantes')
    print('3. Altenar o estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu():
    input('Digite uma tecla para voltar ao menu principal! ')
    main()

def opção_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
     os.system('clear')
     linha = '*' * (len(texto) + 4)
     print(linha)
     print(texto)
     print(linha)
     print()

def Cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes:')
    print()
    nome_restaurante = input('escreva o nome do restaurante:\n')
    categoria = input('Digite o nome da categoria do restaurante {}: '.format(nome_restaurante))
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print('O Restaurante {} foi cadastrado com sucesso\n'.format(nome_restaurante))

    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando todos os restaurantes')
    print('{} | {} | {}\n'.format('NOME DO RESTAURANTE'.ljust(20), 'CATEGORIA DO RESTAURANTE'.ljust(20), 'STATUS DO RESTAURANTE'))
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print('{} | {} | {}\n'.format(nome_restaurante.ljust(20), categoria.ljust(24), ativo))
    
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restuarante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restuarante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = 'O restaurante {} foi ativado com sucesso'.format(nome_restuarante) if restaurante['ativo'] else 'O restaurante {} foi desativado com suscesso!'.format(nome_restuarante)
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()





def esolher_opções():
    try:
        opção_escolhida = int(input('Escolha uma das opções?\n'))
        if opção_escolhida == 1:
            Cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
             alternar_estado_restaurante()
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opção_invalida()
    except:
        opção_invalida()
            
        

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opções()
    esolher_opções()


if __name__ == '__main__':
    main()

