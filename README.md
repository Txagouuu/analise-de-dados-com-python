# Sistema CRUD em Python

Este projeto é uma aplicação **CRUD (Create, Read, Update, Delete)** desenvolvida em Python para gerenciamento de usuários utilizando persistência de dados em arquivo JSON.

## 📁 Estrutura do Projeto
```
ANALISE-DE-DADOS-COM-PYTHON/
├── actions/
│   ├── create.py   # Função para criar usuários
│   ├── delete.py   # Função para excluir usuários
│   ├── edit.py     # Função para editar dados de usuários
│   ├── load.py     # Carrega e gerencia dados do JSON
│   └── print.py    # Exibe a lista de usuários
├── cadastros.json  # Banco de dados em formato JSON
├── usuario.py      # Classe Usuario com regras de negócio
├── main.py         # Arquivo principal para execução do sistema
├── requirements.txt# Dependências do projeto
├── LICENSE         # Licença do projeto
└── README.md       # Documentação do projeto
```

## 🚀 Funcionalidades
- ✅ Adicionar novos usuários
- 📄 Listar usuários cadastrados
- ✏️ Editar informações existentes
- ❌ Excluir usuários do sistema
- 💾 Todos os dados são armazenados em `cadastros.json`

## 🧠 Tecnologias Utilizadas
- Python 3.x
- Manipulação de Arquivos JSON
- Programação Orientada a Objetos (POO)

## ▶️ Como Executar o Projeto
```bash
# Clonar o repositório
git clone https://github.com/Txagouuu/analise-de-dados-com-python.git

# Acessar o diretório
cd ANALISE-DE-DADOS-COM-PYTHON

# Ativar ambiente virtual (se houver)
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar o sistema
python main.py
```

## 🔧 Estrutura do Arquivo JSON (`cadastros.json`)
```json
{
    "id": 6,
    "nome": "teste",
    "idade": 999,
    "email": "teste@gmail.com",
    "telefone": "5599999",
    "cidade": "teste-city",
    "cpf": null,
    "ativo": true,
    "endereco": null
}
```

## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, ajustes ou novas funcionalidades.

---
📌 **Autor:** Tiago Mendonça
📌 **Licença:** Este projeto está licenciado sob os termos da licença MIT.

