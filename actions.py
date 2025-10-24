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

        


def atualizar_dados_usuario(id_usuario):
    """Atualiza os dados de um usuário existente."""
    # garante banco carregado
    if not usuario.banco_usuarios:
        carregar_DB()

    # tenta normalizar id para inteiro quando possível
    try:
        id_int = int(id_usuario)
    except Exception:
        id_int = None

    usuario_encontrado = None
    for u in usuario.banco_usuarios:
        u_id = getattr(u, "id", getattr(u, "_id", None))
        try:
            if id_int is not None and int(u_id) == id_int:
                usuario_encontrado = u
                break
        except Exception:
            if str(u_id) == str(id_usuario):
                usuario_encontrado = u
                break

    if usuario_encontrado is None:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        return

    print(f"Atualizando dados do usuário com ID: {getattr(usuario_encontrado,'id', getattr(usuario_encontrado,'_id', 'N/A'))}, Nome: {getattr(usuario_encontrado,'nome','')}, Ativo: {getattr(usuario_encontrado,'_ativo','')}")

    while True:
        print("\nO que você deseja alterar?")
        print("1. Nome")
        print("2. Idade")
        print("3. Email")
        print("4. Telefone")
        print("5. Cidade")
        print("6. Status Ativo/Inativo")
        print("7. Voltar ao Menu Principal")
        print("---------------------------------------------")

        try:
            escolha = int(input("Escolha uma opção (1-7): "))
        except ValueError:
            print("Entrada inválida. Informe um número correspondente à opção.")
            continue

        if escolha == 1:
            novo = input("Novo nome (aperte Enter para manter): ").strip()
            if novo:
                usuario_encontrado.nome = novo
                print("Nome atualizado.")
        elif escolha == 2:
            entrada = input("Nova idade (aperte Enter para manter): ").strip()
            if entrada:
                try:
                    nova_idade = int(entrada)
                    if nova_idade > 0:
                        usuario_encontrado.idade = nova_idade
                        print("Idade atualizada.")
                    else:
                        print("Idade deve ser positiva.")
                except ValueError:
                    print("Entrada inválida. Idade deve ser um número inteiro.")
        elif escolha == 3:
            novo = input("Novo email (aperte Enter para manter): ").strip()
            if novo:
                usuario_encontrado.email = novo
                print("Email atualizado.")
        elif escolha == 4:
            novo = input("Novo telefone (aperte Enter para manter): ").strip()
            if novo:
                usuario_encontrado.telefone = novo
                print("Telefone atualizado.")
        elif escolha == 5:
            novo = input("Nova cidade (aperte Enter para manter): ").strip()
            if novo:
                usuario_encontrado.cidade = novo
                print("Cidade atualizada.")
        elif escolha == 6:
            # valida input de status
            while True:
                print("S para Ativar a conta")
                print("N para Desativar a conta")
                nova_status = input("Alterar estado? (S/N) [Enter mantém]: ").strip().lower()
                if nova_status in ("s", "n", ""):
                    break
                print("Entrada inválida. Digite 'S' para sim, 'N' para não ou Enter para manter.")
            if nova_status == "s":
                usuario_encontrado.ativar_conta()
                           
            elif nova_status == "n":
                usuario_encontrado.desativar_conta()
                
            else:
                print("Status mantido.")
        elif escolha == 7:
            print("Retornando ao menu principal...")
            menu()
            break
        else:
            print("Opção inválida. Tente novamente.")

        # salva após cada alteração
        try:
            usuario.salvar_banco_json()
        except Exception as e:
            print(f"Aviso: falha ao salvar alterações: {e}")

def deletar_usuario(id_usuario):
    """Remove um usuário por ID (pede confirmação) e salva o arquivo.
    Se id_usuario for None, pede ao usuário até encontrar ou cancelar (Enter)."""
    # garante banco carregado
    if not usuario.banco_usuarios:
        carregar_DB()

    while True:
        # se id não vier por parâmetro, pede ao usuário
        if id_usuario == "":
            print("Operação cancelada.")
            return
        # Opção 1: usando .isnumeric() — aceita apenas inteiros positivos (sem sinal)
        if not id_usuario.isnumeric():
            print("ID inválido. Informe um número inteiro positivo.")
            return
            # repetir pergunta ou continuar o loop
        else:
            id_int = int(id_usuario)
            # prosseguir com a busca/exclusão

        # tenta normalizar id para inteiro quando possível
        try:
            id_int = int(id_usuario)
        except Exception:
            id_int = None

        found_index = None
        for idx, u in enumerate(usuario.banco_usuarios):
            u_id = getattr(u, "id", getattr(u, "_id", None))
            try:
                if id_int is not None and int(u_id) == id_int:
                    found_index = idx
                    break
            except Exception:
                if str(u_id) == str(id_usuario):
                    found_index = idx
                    break

        if found_index is None:
            print(f"Usuário com ID {id_usuario} não encontrado. Tente novamente ou digite Enter para cancelar.")
            id_usuario = None
            continue

        # usuário encontrado — mostra dados e pede confirmação
        u = usuario.banco_usuarios[found_index]
        print("Usuário encontrado:")
        print(f" ID: {getattr(u,'id', getattr(u,'_id','N/A'))}")
        print(f" Nome: {getattr(u,'nome','')}")
        print(f" Email: {getattr(u,'email','')}")
        print(f" Ativo: {getattr(u,'ativo', getattr(u,'_ativo', True))}")

        while True:
            confirmar = input("Confirma exclusão deste usuário? (S/N): ").strip().lower()
            if confirmar in ("s", "n"):
                break
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")

        if confirmar == "s":
            del usuario.banco_usuarios[found_index]
            try:
                usuario.salvar_banco_json()
                print("Usuário excluído com sucesso.")
            except Exception as e:
                print(f"Aviso: não foi possível salvar alterações: {e}")
        else:
            print("Exclusão cancelada.")
        return

def menu():
    """Exibe o menu principal da aplicação."""

    print("\n--- Sistema de Cadastro de Clientes (v2.0) ---")
    print("1. Adicionar Cliente")
    print("2. Listar Todos os Clientes")
    print("3. Atualizar Dados de Cliente")
    print("4. Deletar úsuario")
    print("5. Sair")
    print("---------------------------------------------")
