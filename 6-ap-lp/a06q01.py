def mensagem():
    return input("Digite uma mensagem: ")

def num():
    return int(input("Digite um numero: "))

if __name__ == "__main__":
    print(mensagem(), num())
'''
def exibir_mensagem(mensagem, numero):
    """
    Função que exibe uma mensagem e um número, sem retornar nada.
    
    Args:
        mensagem (str): A mensagem a ser exibida.
        numero (int/float): O número a ser exibido.
    """
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def main():
    """
    Função principal que lê os dados do usuário e chama exibir_mensagem.
    """
    mensagem = input("Digite uma mensagem: ")
    numero = float(input("Digite um número: "))  # Usando float para aceitar números decimais
    exibir_mensagem(mensagem, numero)

if __name__ == "__main__":
    main()
