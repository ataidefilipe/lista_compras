from class_lista import ListaDeCompras

lista = ListaDeCompras()

if __name__ == "__main__":
    while True:
        print("\nLista de compras:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Marcar como comprado")
        print("4. Exibir lista")
        print("5. Sair")

        user = input("Escolha uma opção: ")

        if user == '1':
            item = input("Digite o nome do item que quer adicionar na lista: ")
            quantidade = int(input("Digite a quantidade: "))
            try:
                lista.adicionar_item(item, quantidade)
                print(f"{quantidade} de {item} adicionado(s) a lista")
            except ValueError as e:
                print(e)
        
        elif user == '2':
            item = input("Digite o nome do item que quer subtrair da lista: ")
            quantidade = int(input("Digite a quantidade do item a ser subtraido: "))
            try:
                lista.remover_quantidade(item, quantidade)
                print(f"{quantidade} de {item} removido(s) da lista")
            except ValueError as e:
                print(e)
            except KeyError as e:
                print(e)
        
        elif user == '3':
            item = input("Digite o nome do item que quer marcar como comprado: ")
            try:
                lista.marcar_comprado(item)
                print(f"{item} marcado como comprado e removido da lista")
            except KeyError as e:
                print(e)
        
        elif user == '4':
            itens = lista.listar_itens()
            if not itens:
                print("A lista de compras está vazia.")
            else:
                print("\nItens identificados na lista")
                for i in itens:
                    print(f"- {i}: {itens[i]}")