from usuario import usuario
import json

def carregar_DB(caminho_arquivo='cadastros.json'):
    """Carrega cadastros.json e popula usuario.banco_usuarios com instâncias."""
    usuario.banco_usuarios.clear()
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    for d in dados:
        u = usuario(
            d.get('id'),
            d.get('nome'),
            d.get('idade'),
            d.get('email'),
            d.get('telefone'),
            cpf=d.get('cpf'),
            cidade=d.get('cidade'),
            ativo=d.get('ativo', True)
        )
        usuario.banco_usuarios.append(u)
    return len(usuario.banco_usuarios)