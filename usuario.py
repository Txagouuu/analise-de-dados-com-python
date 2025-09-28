import json
class usuario:
    banco_usuarios = []
    def __init__(self, nome,idade,email,telefone,endereco,data_cadastro=None,atiivo=True):
        self._nome = nome
        self._idade = idade
        self._email = email
        self._telefone = telefone
        self._endereco = endereco
        self._data_cadastro = data_cadastro
        self._ativo = atiivo
    
    def __str__(self):
        return f"Nome: {self._nome} , Ativo: {self._ativo}"
    
    def desativar_conta(self):
        self._ativo = False
        print("Conta desativada com sucesso.")

    def ativar_conta(self):
        self._ativo = True
        print("Conta ativada com sucesso.")
    
    @classmethod
    def criar_usuario(cls, nome, idade, email, telefone, endereco):
        usuario_novo = cls(nome, idade, email, telefone, endereco)
        cls.banco_usuarios.append(usuario_novo)
        print(f"Usuário {nome} criado com sucesso.")

    @classmethod
    def salvar_banco_json(cls, arquivo="cadastros.json"):
        """Salva todos os usuários da lista em um arquivo JSON"""
        dados = []
        for u in cls.banco:
            dados.append({
                "nome": u.nome,
                "idade": u.idade,
                "email": u.email,
                "telefone": u.telefone,
                "endereco": u.endereco,
                "data_cadastro": u.data_cadastro,
                "ativo": u.ativo
            })
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"{len(cls.banco)} usuário(s) salvo(s) em {arquivo}")