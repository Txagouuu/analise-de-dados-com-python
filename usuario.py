import json
class usuario:
    banco_usuarios = []
    banco = banco_usuarios  # <-- alias para compatibilidade com código antigo
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
        novo_id = len(cls.banco_usuarios) + 1
        # passa cpf explicitamente como None e cidade por keyword para mapear corretamente
        usuario_novo = cls(novo_id, nome, idade, email, telefone, cpf=None, cidade=cidade)
        cls.banco_usuarios.append(usuario_novo)
        print(f"Usuário {nome} criado com sucesso.")

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

