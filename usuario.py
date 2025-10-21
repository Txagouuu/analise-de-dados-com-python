import json
class usuario:
    banco_usuarios = []
    def __init__(self,id, nome,idade,email,telefone,cpf=None, cidade=None,ativo=True):
        self._nome = nome
        self._idade = idade
        self._email = email
        self._telefone = telefone
        self._cidade = cidade
        self._cpf = cpf
        self._id = id
        self._ativo = ativo


    
    def desativar_conta(self):
        self._ativo = False
        print("Conta desativada com sucesso.")

    def ativar_conta(self):
        self._ativo = True
        print("Conta ativada com sucesso.")
    
    @classmethod
    def criar_usuario(cls, nome, idade, email, telefone, cidade):
        novo_id = len(cls.banco_usuarios) + 1
        usuario_novo = cls(novo_id,nome, idade, email, telefone, cidade)
        cls.banco_usuarios.append(usuario_novo)
        print(f"Usuário {nome} criado com sucesso.")

    @classmethod
    def salvar_banco_json(cls, arquivo="cadastros.json"):
        """Salva todos os usuários da lista em um arquivo JSON"""
        dados = []
        for u in cls.banco_usuarios:
            dados.append({
                "nome": u.nome,
                "idade": u.idade,
                "email": u.email,
                "telefone": u.telefone,
                "endereco": u.endereco,
                "cidade": u.cidade,
                "ativo": u.ativo
            })
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"{len(cls.banco)} usuário(s) salvo(s) em {arquivo}")

    