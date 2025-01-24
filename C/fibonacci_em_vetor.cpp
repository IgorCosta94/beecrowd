#include <stdio.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int a = 0; a < t; a++) {
        long int x;
        scanf("%d", &x);

        x = abs(x);
        double n1 = 0.0, n2 = 1.0;
		double soma = 0.0;

        if (x == 0) {
            printf("Fib(0) = 0\n");
        } else if (x == 1) {
            printf("Fib(1) = 1\n");
        } else if (x > 1) {
            for (int b = 2; b <= x; b++) {
                soma = n1 + n2;
                n1 = n2;
                n2 = soma;
            }
            printf("Fib(%d) = %.0lf\n", x, soma);
        }
    }

    return 0;
}

