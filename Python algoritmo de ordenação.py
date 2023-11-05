def insertion_sort(vetor):
    tamanho = len(vetor)
    
    for i in range(1, tamanho):
        atual = vetor[i]
        j = i - 1
        
        while j >= 0 and vetor[j] > atual:
            vetor[j + 1] = vetor[j]
            j -= 1
        
        vetor[j + 1] = atual
    
    return vetor


def main():
    tamanho = int(input("Informe o tamanho do vetor: "))
    vetor = []
    
    for i in range(tamanho):
        numero = int(input("Informe um número ímpar: "))
        if numero % 2 == 0:
            print("Erro: o número informado não é ímpar.")
            return
        
        vetor.append(numero)
    
    vetor_ordenado = insertion_sort(vetor)
    print("Vetor ordenado:", vetor_ordenado)


if __name__ == "__main__":
    main()