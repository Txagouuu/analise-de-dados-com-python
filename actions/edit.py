from usuario import usuario
from actions.load import carregar_DB
from actions.print import menu

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
            
            break
        else:
            print("Opção inválida. Tente novamente.")

        # salva após cada alteração
        try:
            usuario.salvar_banco_json()
        except Exception as e:
            print(f"Aviso: falha ao salvar alterações: {e}")
