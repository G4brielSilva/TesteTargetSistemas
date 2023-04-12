#include <stdio.h>

int calculaFibonacci(int numero) {
    int seq = 0;
    int aux = 1;
    while ( seq < numero ) {
        if (seq == 0) {
            aux = 0;
            seq += 1;
        } else {
            aux = seq;
            seq += aux;
        }
    }

    if (! (seq == numero) )
        return 0;
    
    return 1;
}

int main(int argc, char const *argv[]) {
    int numero = 0;
    // scanf("%d",&numero);
    printf("%d",calculaFibonacci(numero));

    return 0;
}
