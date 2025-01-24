#include<stdio.h>

void poligono(void);

int main(void){
	poligono();
	return 0;
}

void poligono(void){
	long int a,b;
	scanf("%li %li", &a, &b);
	
	printf("%li\n", a*b);
}
