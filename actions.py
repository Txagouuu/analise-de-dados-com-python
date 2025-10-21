
from usuario import usuario
import json


def adicionar_usuario():
    """Adiciona um novo usuário ao banco de dados."""
    print("Adicionando novo usuário...")
    while True:
        try:
            # Pede todos os dados de uma vez
            nome = input("Nome: ").strip()
            if not nome:
                raise ValueError("O nome não pode ser vazio.")

            idade_str = input("Idade: ").strip()
            if not idade_str:
                raise ValueError("A idade não pode ser vazia.")
            idade = int(idade_str) # Tenta converter para inteiro
            if idade <= 0:
                raise ValueError("A idade deve ser um número positivo.")

            email = input("Email: ").strip()
            if not email:
                raise ValueError("O email não pode ser vazio.")

            telefone = input("Telefone: ").strip()
            if not telefone:
                raise ValueError("O telefone não pode ser vazio.")

            cidade = input("Cidade: ").strip()
            if not cidade:
                raise ValueError("A cidade não pode ser vazia.")

            # Se todas as validações passaram, sai do loop
            break

        except ValueError as e:
            # Se qualquer validação falhar, imprime o erro e o loop recomeça
            print(f"Erro de entrada: {e}. Por favor, tente novamente.")
            print("----------------------------------------------------")

    # Após o loop ser quebrado (dados válidos), cria e salva o usuário
    usuario.criar_usuario(nome, idade, email, telefone, cidade)
    usuario.salvar_banco_json()
    print("\n--- Usuário adicionado com sucesso! ---")



def carregar_e_listar_usuarios(caminho_arquivo='cadastros.json'):
    """Carrega usuários de um arquivo JSON e os imprime."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_json = json.load(f)
        
        lista_de_usuarios = []
        for dados_usuario in dados_json:
            
            novo_usuario = usuario(
                id=dados_usuario.get('id'),
                nome=dados_usuario.get('nome'),
                idade=dados_usuario.get('idade'),
                email=dados_usuario.get('email'),
                telefone=dados_usuario.get('telefone'),
                cpf=dados_usuario.get('cpf'),
                cidade=dados_usuario.get('cidade'),
                ativo=dados_usuario.get('ativo', True)
            )
            lista_de_usuarios.append(novo_usuario)
        
        # Imprime os detalhes de cada usuário
        for u in lista_de_usuarios:
            print("----- Usuário -----")
            print(f" ID: {u._id}\n Nome: {u._nome}\n Email: {u._email}\n Ativo: {u._ativo}")
            print("-------------------\n")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Falha ao decodificar o JSON do arquivo '{caminho_arquivo}'.")
