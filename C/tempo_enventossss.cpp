#include <stdio.h>

int main() {
    int dia, horas, minutos, segundos;
    int diat, horast, minutost, segundost;
    int total, total2, tempo;

    printf("dia ");
    scanf("%d", &dia);
    scanf("%d : %d : %d", &horas, &minutos, &segundos);

    horas *= 3600;
    minutos *= 60;
    total = horas + minutos + segundos;


    printf("dia ");
    scanf("%d", &diat);
    scanf("%d : %d : %d", &horast, &minutost, &segundost);

    diat = (diat - dia) * 86400;
    horast *= 3600;
    minutost *= 60;
    total2 = horast + minutost + segundost;

    tempo = diat - (total - total2);

    if (tempo >= 60) {
        segundos = 0;
        minutos = 0;
        horas = 0;
        dia = 0;
        int x = 0;

        while (tempo >= 0) {
            if (x < 60 && tempo < 60) {
                segundos = x;
            }
            if (x == 60 && tempo < 3600) {
                minutos += 1;
                x = 0;
            }
            if (tempo >= 3600) {
                horas += 1;
                tempo -= 3600;
            }
            if (tempo >= 86400) {
                dia += 1;
                tempo -= 86400;
            }

            tempo -= 1;
            x += 1;
        }

        printf("%d dia(s)\n", dia);
        printf("%d hora(s)\n", horas);
        printf("%d minuto(s)\n", minutos);
        printf("%d segundo(s)\n", segundos);
    }

    return 0;
}

