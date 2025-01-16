import random
import string

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    """Gera a de acordo com as especificações passadas pelo usuário"""

    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres +=  string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("====================================")
    print("          GERADOR DE SENHAS         ")
    print("====================================")

    tamanho = int(input("\nDigite o tamanho da senha: "))
    usar_maiusculas = input("Inserir letras maiúsculas? (S/N): ").strip().lower() == 's'
    usar_numeros = input("Inserir números? (S/N): ").strip().lower() == 's'
    usar_simbolos = input("Inserir símbolos? (S/N): ").strip().lower() == 's'

    senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
    print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    main()
        