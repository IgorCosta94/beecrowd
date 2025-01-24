#include<stdio.h>

int main(void){
	int i = 1;
	int j = 7, m = j;
	int cont = 0;
	for( int w = 1 ; w <= 15 ; w += 1){
		if(cont == 3){
			i += 2;
			m += 2;
			j = m;
			cont = 0;
		}
		cont += 1;
		printf("I=%d J=%d\n", i ,j--);
	}

	return 0;
}
