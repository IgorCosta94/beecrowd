#include <stdio.h>
#include <time.h>

int main(void) {
    struct tm tempo = {0}, tempo0 = {0};

    // Inicialização da primeira estrutura
    tempo.tm_sec = 84; // 84 segundos (será ajustado por mktime para 1 minuto e 24 segundos)
    tempo.tm_min = 1;
    tempo.tm_hour = 1;
    tempo.tm_mday = 1;
    tempo.tm_mon = 1;   // Fevereiro (os meses começam em 0)
    tempo.tm_year = 1;  // Ano 1901 (anos desde 1900)

    // Inicialização da segunda estrutura
    tempo0.tm_sec = 42; // 42 segundos
    tempo0.tm_min = 1;
    tempo0.tm_hour = 1;
    tempo0.tm_mday = 1;
    tempo0.tm_mon = 1;   // Fevereiro
    tempo0.tm_year = 1;  // Ano 1901

    // Calculando a diferença em segundos
    double diferenca = difftime(mktime(&tempo),mktime(&tempo0));
    printf("Diferença: %.0f segundos\n", diferenca);

    return 0;
}

