from catalogo import catalogo

while True:
    #area para configuração de carrinho
    carrinho = {
        
    }
    taxaGarcom = 0.10
    #bloco de opçoes para o usuario
    print("1 - Função ADM")
    print("2 - Cliente")
    opcao = input("Escolha uma opção: ")

    #tratando as opçoes iniciais
    if opcao == "1":
        while True:
            print("Cardápio atual:")
            #iniiando um loop para percorrer todas as categorias e respectivos itens.
            for categoria, itens in catalogo.items():
                print(f"{categoria}:")

                #iniciando um loop para percorrer as subcategorias e seus respectivos itens.
                for subcategoria, produtos in itens.items():
                    print(f"  {subcategoria}:")
                    #iniciando um loop para percorrer os produtos e os preços.
                    for produto, preco in produtos.items():
                        print(f"    {produto} R${preco}")
            print()
            
            #apó mostrar a catalogo nós iniciamos o processo de configuração do adm
            print("1 - Adicionar item")
            print("2 - Alterar item")
            print("3 - Excluir item")
            print("4 - Voltar")
            opcaoAdm = input("Escolha uma opção: ")

            #tratando as opçoes

            #Adicionando itens
            if opcaoAdm == "1":
                categoria = input("Digite a categoria do item: ")
                subcategoria = input("Digite a subcategoria do item: ")
                produto = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                #abaixo tratamos algumas falhas, como a de não existir a categoria ou a sub
                if categoria not in catalogo:
                    catalogo[categoria] = {}
                if subcategoria not in catalogo[categoria]:
                    catalogo[categoria][subcategoria] = {}
                #aqui atualizamos o catalogo com as informaçoes passadas la em cima
                catalogo[categoria][subcategoria][produto] = preco


                # alterando produto
            elif opcaoAdm == "2":
                categoria = input("Digite a categoria do item: ")
                subcategoria = input("Digite a subcategoria do item: ")
                produto = input("Digite o nome do produto: ")
                #aqui verificamos se a categoria, subcategoria e produto estao no catalogo, serve como um tratamento de erro
                if categoria in catalogo and subcategoria in catalogo[categoria] and produto in catalogo[categoria][subcategoria]:
                    novoPreco = float(input("Digite o novo preço do produto: "))
                    catalogo[categoria][subcategoria][produto] = novoPreco
                else:
                    print("Item não encontrado.")
            


            #aqui estamos deletando itens
            elif opcaoAdm == "3":
                categoria = input("Digite a categoria do item: ")
                subcategoria = input("Digite a subcategoria do item: ")
                produto = input("Digite o nome do produto: ")

                #verificando se categoria, subcategoria e produto estao no catalogo, e usando a função 'del' para excluir do dicionario.
                if categoria in catalogo and subcategoria in catalogo[categoria] and produto in catalogo[categoria][subcategoria]:
                    del catalogo[categoria][subcategoria][produto]
                else:
                    print("Item não encontrado.")
                
            #aqui tratamos a opção de finalização/retorno 
            elif opcaoAdm == "4":
                break

    # a seguir vem o codigo para gerenciar as opçoes do cliente
    
    elif opcao == "2":
        while True:


            print("Categorias:")
            #aqui é feito um loop, no qual usando o enumerate, iremos percorrer cada uma das categorias, e obter um indice em cada uma das iteraçoes, de acordo com a categoria.
            for i, categoria in enumerate(catalogo, start=1):
                print(f"{i} - {categoria}")
            escolha = int(input("Escolha uma categoria: "))
            #aqui armazenamos a categoria escolhida, usando o numero do input do usario, para selecionar na lista, que é formada pelas keys do catalogo, logo o indice da lista que esta diminuido por 1, é o indice da categoria correspondente
            categoriaEscolhida = list(catalogo.keys())[escolha-1]


            print("Subcategorias:")
            #aqui iremos armazenar a subcategoria, que é correspondida pelo indice (categoriaEscolhida), dentro de catalogo, que no caso vai corresponder as subcategorias dentro da categgoria
            subcategorias = catalogo[categoriaEscolhida]
            
            for i, subcategoria in enumerate(subcategorias, start=1):
                print(f"{i} - {subcategoria}")
            escolha = int(input("Escolha uma subcategoria: "))
            subcategoriaEscolhida = list(subcategorias.keys())[escolha-1]

            print("Produtos:")
            produtos = catalogo[categoriaEscolhida][subcategoriaEscolhida]
            for i, produto in enumerate(produtos, start=1):
                print(f"{i} - {produto} R${produtos[produto]}")
            escolha = int(input("Escolha um produto para adicionar ao carrinho: "))
            produtoEscolhido = list(produtos.keys())[escolha-1]

            #abaixo acessamos o valor do produto que foi escolhido
            precoProdutoEscolhido = produtos[produtoEscolhido]

            #aqui verificamos se o produto esta ou não no carrinho, e adicionamos o valor novo se não estiver, e se ja estiver somamos co o valor anterior
            if produtoEscolhido not in carrinho:
                carrinho[produtoEscolhido] = precoProdutoEscolhido
            else:
                carrinho[produtoEscolhido] += precoProdutoEscolhido

            #aqui usamos a função sum para somar todos os valores do objeto
            total = sum(carrinho.values())

            #aqui multiplicamos para estabelecer a taxa
            taxa = total * taxaGarcom

            print(f"Foi adicionado o produto {produtoEscolhido} ao seu carrinho")
            print(f"O total do seu carrinho no momento, com a taxa de 10% do garçom é de R${total+taxa}")            

            print()
            print()



            #abaixo a gente tem opçoes de ação para voltar ou sair
            print("1 - Voltar")
            print("2 - Sair")
            opcaoCliente = input("Escolha uma opção: ")

            #o continue faz com que o programa volte para a iteração inicial do loop e o break fara finalizar tudo, voltando para o "menu principal"
            if opcaoCliente == "1":
                continue
            elif opcaoCliente == "2":
                break
