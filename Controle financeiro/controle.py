import json
import os

ARQUIVO_H = r'gastos.json'

def carregar_gasto():
    if os.path.exists(ARQUIVO_H):
        with open(ARQUIVO_H, 'r') as arquivo:
            return json.load(arquivo)
    return {'gastos': [] , 'limite': 0}

def salvar_gastos(dados):
    with open(ARQUIVO_H, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    

def visualizar_gastos():
    dados = carregar_gasto()

    total = sum(g['valor'] for g in dados['gastos'])

    for g in dados["gastos"]:
        print(f"- R$: {g['valor']:.2f} | Categoria: {g['categoria']} | Data: {g['data']}")
    print(f"Total de gastos: R$ {total} ")

    if dados['limite'] > 0  and total > dados['limite']:
        print("Você ultrapassou o seu limite de gastos!!!")

def adicionar_gasto(valor, categoria, data):
    dados = carregar_gasto()

    dados['gastos'].append({'valor':valor, 'categoria':categoria, 'data':data})
    salvar_gastos(dados)
    print(f"O gasto no valor de {valor:.2f} reais em '{categoria}' foi registrado com sucesso!")

def definir_limite(novo_limite):
    dados = carregar_gasto()

    dados['limite'] = novo_limite
    salvar_gastos(dados)
    print(f"Novo limite de gastos definido em R${novo_limite:.2f} ")

def main():
    while True:
        print("------ Controle de Gastos ------")
        print("1 - Adicionar gasto")
        print("2 - Visualizar gastos")
        print("3 - Defininir limite de gastos")
        print("4 - Sair")
    
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            valor = float(input("Valor(R$): "))
            categoria = input("Categoria do gasto: ")
            data = input("Data (DD/MM/AA): ")

            adicionar_gasto(valor, categoria, data)

        elif escolha == 2:
            visualizar_gastos()

        elif escolha == 3:
            novo_limite = float(input("Limite de gastos: "))

            definir_limite(novo_limite)
        
        elif escolha == 4:
            print("Tchau")
            break

        else:
            print("Comando Incorreto")

main()


