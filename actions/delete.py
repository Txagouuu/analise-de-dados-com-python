from usuario import usuario
from actions.load import carregar_DB
from time import sleep

def deletar_usuario(id_usuario):
    """Remove um usuário por ID (pede confirmação) e salva o arquivo.
    Se id_usuario for None, pede ao usuário até encontrar ou cancelar (Enter)."""
    
    # garante banco carregado
    if not usuario.banco_usuarios:
        carregar_DB()

    # Variável para controlar o ID que estamos buscando.
    # Começa com o parâmetro, mas pode ser atualizada pelo input.
    id_para_buscar = id_usuario 

    while True:
        # --- 1. FASE DE OBTER O ID ---
        
        # Se o ID para buscar for None (veio como parâmetro ou não foi encontrado
        # na rodada anterior), pedimos ao usuário.
        if id_para_buscar is None:
            id_para_buscar = input("Digite o ID do usuário que deseja deletar (ou Enter para cancelar): ").strip()

        # Se o ID (vindo do input ou do parâmetro) for uma string vazia, cancela.
        if id_para_buscar == "":
            print("Operação cancelada.")
            return

        
        found_index = None
        # Convertemos o ID de busca para int *uma vez* se for possível
        id_busca_int = None
        if isinstance(id_para_buscar, str) and id_para_buscar.isnumeric():
            id_busca_int = int(id_para_buscar)
        elif isinstance(id_para_buscar, int):
            id_busca_int = id_para_buscar

        for idx, u in enumerate(usuario.banco_usuarios):
            u_id = getattr(u, "id", getattr(u, "_id", None))
            
            try:
            # 1. Tenta comparar como inteiros
                if id_busca_int is not None and int(u_id) == id_busca_int:
                    found_index = idx
                    break  # Encontrou, sai do loop 'for'
                
            except (ValueError, TypeError):
                pass 

            if str(u_id) == str(id_para_buscar):
                found_index = idx
                break # Encontrou, sai do loop 'for'

        # --- 3. FASE DE RESULTADO ---

        if found_index is None:
            print(f"Usuário com ID {id_para_buscar} não encontrado. Tente novamente ou digite Enter para cancelar.")
            # Define como None para que o loop peça um novo ID na próxima iteração
            id_para_buscar = None 
            continue # Volta ao início do 'while True'

        # --- 4. FASE DE CONFIRMAÇÃO (Só chega aqui se encontrou) ---
        
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
        
        # A operação terminou (seja por exclusão ou cancelamento),
        # então saímos da função.
        sleep(2)
        return
