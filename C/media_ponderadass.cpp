#include <stdio.h>

int main() {
    int n, cont = 1;
    float total = 0;
    float x1,x2,x3;
    float peso[] = {2, 3, 5};

    scanf("%d", &n);

    while (cont <= n) {
        scanf("%f%f%f", &x1,&x2,&x3);
        total = (x1 * peso[0] + x2 * peso[1] + x3 * peso[2])/10;
    	printf("%.1f\n",total);
        cont++;
    }

    return 0;
}

