import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criação da tabela (se não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")
conn.commit()

# Função para adicionar produto
def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conn.commit()
    print("Produto adicionado com sucesso!\n")

# Função para listar produtos
def listar_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    
    if produtos:
        print("\nLista de Produtos:")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]:.2f}, Quantidade: {produto[3]}")
    else:
        print("\nNenhum produto cadastrado.\n")

# Função para atualizar produto
def atualizar_produto():
    id_produto = int(input("ID do produto que deseja atualizar: "))
    novo_nome = input("Novo nome: ")
    novo_preco = float(input("Novo preço: "))
    nova_quantidade = int(input("Nova quantidade: "))

    sql = "UPDATE produtos SET nome = ?, preco = ?, quantidade = ? WHERE id = ?"
    cursor.execute(sql, (novo_nome, novo_preco, nova_quantidade, id_produto))
    conn.commit()
    print("Produto atualizado com sucesso!\n")

# Função para deletar produto
def deletar_produto():
    id_produto = int(input("ID do produto que deseja deletar: "))
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    print("Produto deletado com sucesso!\n")

# MENU PRINCIPAL
while True:
    print("=== MENU ===")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        adicionar_produto()
    elif escolha == "2":
        listar_produtos()
    elif escolha == "3":
        atualizar_produto()
    elif escolha == "4":
        deletar_produto()
    elif escolha == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
