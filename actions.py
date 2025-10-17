
from usuario import usuario
import json


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