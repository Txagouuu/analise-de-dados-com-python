import json
from usuario import usuario
from actions.load import carregar_DB
def listar_usuarios(caminho_arquivo='cadastros.json'):
    """Carrega usuários de um arquivo JSON e os imprime."""
    carregar_DB(caminho_arquivo)
        # Imprime os detalhes de cada usuário
    if not usuario.banco_usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuario.banco_usuarios:
            uid = getattr(u, "id", getattr(u, "_id", "N/A"))
            nome = getattr(u, "nome", "")
            idade = getattr(u, "idade", "")
            email = getattr(u, "email", "")
            telefone = getattr(u, "telefone", "")
            cidade = getattr(u, "cidade", "")
            ativo = getattr(u, "ativo", getattr(u, "_ativo", True))

            print("----- Usuário -----")
            print(f" ID: {uid}")
            print(f" Nome: {nome}")
            print(f" Idade: {idade}")
            print(f" Email: {email}")
            print(f" Telefone: {telefone}")
            print(f" Cidade: {cidade}")
            print(f" Ativo: {ativo}")
            print(f" Endereço: {getattr(u, 'endereco', '')}")
            print("-------------------\n")


def menu():
    """Exibe o menu principal da aplicação."""

    print("\n--- Sistema de Cadastro de Clientes (v2.0) ---")
    print("1. Adicionar Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Atualizar Dados de Cliente")
    print("4. Deletar úsuario")
    print("5. Sair")
    print("---------------------------------------------")