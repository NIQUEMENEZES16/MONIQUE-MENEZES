#[PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.

produtos = {}

for i in range(5):
    nome_produto = input(f"Digite o nome do {i+1}º produto: ")
    preco_produto = float(input(f"Digite o preço do produto {nome_produto}: R$ "))
    produtos[nome_produto] = preco_produto

total_compra = sum(produtos.values())

print("\nResumo da compra:")
for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")

print(f"\nO valor total da compra foi de: R$ {total_compra:.2f}")
