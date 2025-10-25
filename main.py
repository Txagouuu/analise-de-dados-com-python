from usuario import usuario
from actions.print import listar_usuarios
from actions.create import adicionar_usuario
from actions.edit import atualizar_dados_usuario
from actions.print import menu
from actions.delete import deletar_usuario
from actions.load import carregar_DB
import json
from time import sleep

def main():
    """Exibe o menu principal da aplicação."""
    
    # Carrega o banco de dados UMA VEZ ao iniciar o programa
    try:
        total_carregados = carregar_DB()
        print(f"{total_carregados} usuários carregados do arquivo.")
    except Exception as e:
        print(f"Erro ao carregar banco de dados: {e}")
        print("Iniciando com banco de dados vazio.")

    while True:
        menu() # Exibe o menu
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            print("\n[Opção 1: Adicionar Cliente]")
            adicionar_usuario()
            sleep(1.5)

        elif opcao == '2':
            print("\n[Opção 2: Listar Clientes]")
            listar_usuarios()
            input("\nPressione Enter para continuar...") # Pausa

        elif opcao == '3':
            print("\n[Opção 3: Atualizar Cliente]")
            id_para_atualizar = input("Digite o ID do usuário que deseja atualizar: ").strip()
            if id_para_atualizar:
                atualizar_dados_usuario(id_para_atualizar)
            else:
                print("ID inválido ou vazio. Operação cancelada.")
            sleep(1.5)

        elif opcao == '4':
            print("\n[Opção 4: Deletar Usuário]")
           
            deletar_usuario(None)
            sleep(1.5)

        elif opcao == '5':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
            sleep(1)
                



if __name__ == "__main__":
    main()