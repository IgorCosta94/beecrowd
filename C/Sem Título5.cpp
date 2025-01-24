#include <stdio.h>

int main() {
    float I = 0.0;
    float J;

    while (I <= 2.0) {
        for (int k = 1; k <= 3; k++) {
            J = I + k;

            if ((int)(I * 10) % 10 == 0) {
                // Exibe como inteiro se I for 0, 1 ou 2 (arredondado)
                printf("I=%d J=%d\n", (int)I, (int)J);
            } else {
                // Exibe com uma casa decimal para valores intermediários
                printf("I=%.1f J=%.1f\n", I, J);
            }
        }
        I += 0.2;
    }

    return 0;
}
