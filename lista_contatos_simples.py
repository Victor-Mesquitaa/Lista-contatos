
contatos = []

def adicionar_contato():
    """Adiciona um novo contato à lista"""
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"✓ Contato '{nome}' adicionado!\n")

def listar_contatos():
    """Exibe todos os contatos"""
    if len(contatos) == 0:
        print("Nenhum contato cadastrado.\n")
        return
    
    print("\n--- LISTA DE CONTATOS ---")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. {contato['nome']} - {contato['telefone']}")
    print()

def buscar_contato():
    """Busca um contato pelo nome"""
    nome_busca = input("Digite o nome para buscar: ")
    encontrado = False
    
    for contato in contatos:
        if nome_busca.lower() in contato['nome'].lower():
            print(f"Encontrado: {contato['nome']} - {contato['telefone']}\n")
            encontrado = True
    
    if not encontrado:
        print("Contato não encontrado.\n")

def remover_contato():
    """Remove um contato da lista"""
    nome_remover = input("Digite o nome do contato a remover: ")
    
    for contato in contatos:
        if nome_remover.lower() == contato['nome'].lower():
            contatos.remove(contato)
            print(f"✓ Contato '{nome_remover}' removido!\n")
            return
    
    print("Contato não encontrado.\n")

def menu():
    """Exibe o menu principal"""
    while True:
        print("=== LISTA DE CONTATOS ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")
        print()
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            remover_contato()
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
