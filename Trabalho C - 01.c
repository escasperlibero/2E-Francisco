#include <stdio.h>
#include <stdlib.h>

int main() {
    // Criação do ponteiro
    int *ponteiro;

    // Alocação de memória para oito dados inteiros
    ponteiro = (int*) malloc(8 * sizeof(int));

    // Verificação se ocorreu a alocação corretamente
    if (ponteiro == NULL) {
        printf("Erro na alocação de memória.");
        return -1;
    }

    // Realocação de memória para doze dados inteiros
    ponteiro = (int*) realloc(ponteiro, 12 * sizeof(int));

    // Verificação se ocorreu a realocação corretamente
    if (ponteiro == NULL) {
        printf("Erro na realocação de memória.");
        return -1;
    }

    // Liberação do espaço alocado
    free(ponteiro);

    return 0;
}