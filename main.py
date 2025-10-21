from usuario import usuario
from actions import carregar_e_listar_usuarios
from actions import adicionar_usuario
import json

def main():
    """Exibe o menu principal da aplicação."""

    print("\n--- Sistema de Cadastro de Clientes (v2.0) ---")
    print("1. Adicionar Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Atualizar Dados de Cliente")
    print("4. Desativar/Reativar Cliente")
    print("5. Sair")
    print("---------------------------------------------")


    while True:
        try:
            escolha = int(input("Escolha uma opção (1-5): "))
            
            if escolha == 1:
                print("Opção 1 selecionada.")
                adicionar_usuario()
            
            elif escolha == 2:
                print("Opção 2 selecionada.")
                # Chame a função de listar clientes aqui
            elif escolha == 5:
                print("Saindo do sistema...")
                break # Encerra o loop e o programa
            else:
                print("Opção ainda não implementada ou inválida.")
            
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
                



if __name__ == "__main__":
    main()