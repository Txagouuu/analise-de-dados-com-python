from usuario import usuario
from actions.load import carregar_DB
def adicionar_usuario():
    """Adiciona um novo usuário ao banco de dados, validando cada campo individualmente."""
    
    carregar_DB() # Correção importante para não sobrescrever o banco
    print("Adicionando novo usuário...")

    # --- 1. Bloco do NOME ---
    while True:
        nome = input("Nome: ").strip()
        if nome: # Se o nome não for vazio
            break # Sai do loop do nome e continua
        print("Erro de entrada: O nome não pode ser vazio. Tente novamente.")
    
    # --- 2. Bloco da IDADE (validação complexa) ---
    while True:
        idade_str = input("Idade: ").strip()
        if not idade_str:
            print("Erro de entrada: A idade não pode ser vazia. Tente novamente.")
            continue # Pede a idade novamente

        try:
            idade = int(idade_str) # Tenta converter para inteiro
            if idade > 0:
                break # Sucesso! Sai do loop da idade e continua
            else:
                # É um número, mas não é positivo
                print("Erro de entrada: A idade deve ser um número positivo. Tente novamente.")
        except ValueError:
            # O erro que você viu na imagem é capturado aqui
            print(f"Erro de entrada: '{idade_str}' não é um número válido. Tente novamente.")

    # --- 3. Bloco do EMAIL ---
    while True:
        email = input("Email: ").strip()
        if email:
            break
        print("Erro de entrada: O email não pode ser vazio. Tente novamente.")

    # --- 4. Bloco do TELEFONE (Com validação) ---
    while True:
        telefone = input("Telefone: ").strip()
        
        # 1. Verifica se está vazio
        if not telefone:
            print("Erro de entrada: O telefone não pode ser vazio. Tente novamente.")
            continue # Pede o telefone novamente

        # 2. Limpa o telefone de caracteres comuns para verificar os dígitos
        telefone_limpo = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").replace("+", "")

        # 3. Verifica se, após a limpeza, só restaram números
        if not telefone_limpo.isnumeric():
            print(f"Erro de entrada: '{telefone}' contém caracteres inválidos. Use apenas números e os símbolos '()', '-', '+', ' '.")
            continue # Pede o telefone novamente

        # Verifica um comprimento mínimo de dígitos
        if len(telefone_limpo) < 8:
             print(f"Erro de entrada: O telefone parece curto demais. Deve ter pelo menos 8 dígitos.")
             continue # Pede o telefone novamente

        
        break # Sucesso! Sai do loop do telefone

    # --- 5. Bloco da CIDADE ---
    while True:
        cidade = input("Cidade: ").strip()
        if cidade:
            break
        print("Erro de entrada: A cidade não pode ser vazia. Tente novamente.")

    # --- Fim das validações ---

    
    # Cria e salva o usuário
    usuario.criar_usuario(nome, idade, email, telefone, cidade)
    usuario.salvar_banco_json()
    print("\n--- Usuário adicionado com sucesso! ---")