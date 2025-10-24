from usuario import usuario
from actions import listar_usuarios
from actions import adicionar_usuario
from actions import atualizar_dados_usuario
from actions import menu
from actions import deletar_usuario
import json
from time import sleep

def main():
    """Exibe o menu principal da aplicação."""
    menu()


    while True:
        try:
            escolha = int(input("Escolha uma opção (1-5): "))
            
            if escolha == 1:
                print("Opção 1 selecionada.")
                adicionar_usuario()#função de adicionar clientes
            
            elif escolha == 2:
                print("Opção 2 selecionada.")
                listar_usuarios()# função de listar clientes 
                sleep(2)
                menu()
            elif escolha == 3:
                print("Opção 3 selecionada.")
                listar_usuarios()# função de listar clientes
                id_usuario = input("Digite o ID do usuário que deseja deletar (ou Enter para cancelar): ").strip()
                atualizar_dados_usuario(id_usuario)# função de atualizar dados do cliente
            elif escolha == 4:
                print("Opção 4 selecionada.")
                id_usuario = int(input("Digite o ID do usuário que deseja deletar: "))
                deletar_usuario(id_usuario)# função de deletar cliente
            
            elif escolha == 5:
                print("Saindo do sistema...")
                break # Encerra o loop e o programa
            else:
                print("Opção ainda não implementada ou inválida.")
            
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
                



if __name__ == "__main__":
    main()