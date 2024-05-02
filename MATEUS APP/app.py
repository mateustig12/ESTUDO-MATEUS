import os

def exibir_nome_programa():
    print('Sabor express\n')

def exibir_opções():
    print('1. Cadastro de novo restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Finalizando o app\n')

def opção_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def esolher_opções():
    try:
        opção_escolhida = int(input('Escolha uma das opções?\n'))
        if opção_escolhida == 1:
            print('\nCadastrar novo restaurante')
        elif opção_escolhida == 2:
            print('\nListar restaurantes')
        elif opção_escolhida == 3:
            print('\nAtivar restaurante')
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

