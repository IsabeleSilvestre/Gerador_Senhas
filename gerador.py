import random
import string

class GeradorSenha:
    def __init__(self):
        
        self.letras_maiusculas = 0
        self.letras_minusculas = 0
        self.numeros = 0
        self.qtd_caracteres_especiais = 0
        self.caracteres_especiais = "!@#$%&*()_+-=[]{}|;:,.<>?"

    def definir_senha_personalizada(self, qtd_caracteres_especiais, qtd_letras_maiusculas, qtd_letras_minusculas, qtd_numeros):
        self.qtd_caracteres_especiais = qtd_caracteres_especiais
        self.letras_maiusculas = qtd_letras_maiusculas
        self.letras_minusculas = qtd_letras_minusculas
        self.numeros = qtd_numeros

    def gerar_senha_personalizada(self):
        caracteres_especiais = random.choices(self.caracteres_especiais, k=self.qtd_caracteres_especiais)
        letras_maiusculas = random.choices(string.ascii_uppercase, k=self.letras_maiusculas)
        letras_minusculas = random.choices(string.ascii_lowercase, k=self.letras_minusculas)
        numeros = random.choices(string.digits, k=self.numeros)

        senha = caracteres_especiais + letras_maiusculas + letras_minusculas + numeros
        random.shuffle(senha)  

        return "".join(senha)


    def gerar_senha_automatica(self, tamanho_min=12, tamanho_max=15):
        tamanho = random.randint(tamanho_min, tamanho_max)
        
        todos_caracteres = string.ascii_letters + string.digits + self.caracteres_especiais

        senha = [
        random.choice(string.ascii_uppercase),  
        random.choice(string.ascii_lowercase),  
        random.choice(string.digits),           
        random.choice(self.caracteres_especiais or "!@#$%&*()_+-=[]{}|;:,.<>?")

         ]

        for _ in range(tamanho - 4):
            senha.append(random.choice(todos_caracteres))

        random.shuffle(senha)  
        return "".join(senha)  
    
def entrada_usuario():

    while True:
        try:
            qtd_caracteres_especiais = int(input("Digite a quantidade de caracteres especiais que deseja: "))
            qtd_letras_maiusculas = int(input("Digite a quantidade de letras maiúsculas que deseja: "))
            qtd_letras_minusculas = int(input("Digite a quantidade de letras minúsculas que deseja: "))
            qtd_numeros = int(input("Digite a quantidade de números que deseja: "))

            if qtd_caracteres_especiais < 0 or qtd_letras_maiusculas < 0 or qtd_letras_minusculas < 0 or qtd_numeros < 0:
                print("Por favor, insira valores positivos.")
            else:
                return qtd_caracteres_especiais, qtd_letras_maiusculas, qtd_letras_minusculas, qtd_numeros
        except ValueError:
            print("Por favor, insira números válidos.")

def menu():
    
    print("\nEscolha uma opção:")
    print("1. Gerar senha personalizada")
    print("2. Gerar senha automática")
    print("3. Sair")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

if __name__ == "__main__":
    gerador = GeradorSenha()

    while True:
        opcao = menu()

        if opcao == "1":
            preferencias = entrada_usuario()
            gerador.definir_senha_personalizada(*preferencias)
            senha = gerador.gerar_senha_personalizada()
            print("\nSenha Personalizada Gerada:", senha)
        elif opcao == "2":
            senha = gerador.gerar_senha_automatica()
            print("\nSenha Automática Gerada:", senha)
        elif opcao == "3":
            print("Obrigado por usar o Gerador de Senhas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja gerar outra senha? (s/n): ").lower()
        if continuar != "s":
            print("Obrigado por usar o Gerador de Senhas. Até logo!")
            break