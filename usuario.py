import json
class usuario:
    banco_usuarios = []
    banco = banco_usuarios  # maior compatibilidade com código antigo
    def __init__(self,id, nome,idade,email,telefone,cpf=None, cidade=None,ativo=True,endereco=None):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.cidade = cidade
        self._cpf = cpf
        self.id = id
        self._ativo = ativo
        self.endereco = endereco


    
    def desativar_conta(self):
        self._ativo = False
        print("Conta desativada com sucesso.")

    def ativar_conta(self):
        self._ativo = True
        print("Conta ativada com sucesso.")
    
    @classmethod
    def criar_usuario(cls, nome, idade, email, telefone, cidade):
        
        if not cls.banco_usuarios:
            novo_id = 1
        else:
            
            ids_existentes = []
            for u in cls.banco_usuarios:
                try:
                    
                    u_id = int(getattr(u, 'id', getattr(u, '_id', 0)))
                    ids_existentes.append(u_id)
                except (ValueError, TypeError):
                    continue
            
            
            if not ids_existentes:
                novo_id = 1
            else:
                novo_id = max(ids_existentes) + 1
                
    
        usuario_novo = cls(novo_id, nome, idade, email, telefone, cpf=None, cidade=cidade)
        cls.banco_usuarios.append(usuario_novo)
        
        print(f"Usuário {nome} (ID: {novo_id}) criado com sucesso.")
    
    @classmethod
    def salvar_banco_json(cls, arquivo="cadastros.json"):
        """Salva todos os usuários da lista em um arquivo JSON"""
        
        dados = []
        for u in cls.banco_usuarios:
            dados.append({
                "id": getattr(u, "id", getattr(u, "_id", None)),
                "nome": getattr(u, "nome", ""),
                "idade": getattr(u, "idade", ""),
                "email": getattr(u, "email", ""),
                "telefone": getattr(u, "telefone", ""),
                "cidade": getattr(u, "cidade", ""),
                "cpf": getattr(u, "_cpf", None),
                "ativo": getattr(u, "_ativo", getattr(u, "ativo", True)),
                "endereco": getattr(u, "endereco", None)  # seguro se não existir
            })
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("usuário(s) salvo(s)")

