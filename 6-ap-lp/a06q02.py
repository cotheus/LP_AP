def nasc(x, y):
    return y - x

if __name__ == "__main__":
    ano = int(input("Digite o ano de nascimento: "))
    print(f"Voce tem {nasc(ano, 2025)} anos.") 