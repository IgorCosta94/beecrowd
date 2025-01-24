#include<stdio.h>

void dec_hex(void);
int ordem(int *x, int b);

int main(void){
	dec_hex();
	return 0;
}

void dec_hex(void){
	long int v, x;
	int vet[10]={0};
	int cont = 0;
	scanf("%li", &v);
	
	while( v != 0){
		vet[cont]=v%16;
		cont++;
		v /= 16;
	}
	ordem(vet,cont);
}

int ordem(int *x,int c){
	int a;
	
	for(int b=c-1; b >= 0;b-- ){
		switch(x[b]){
			case 10:
				printf("A");
				break;
			case 11:
				printf("B");
				break;
			case 12:
				printf("C");
				break;
			case 13:
				printf("D");
				break;
			case 14:
				printf("E");
				break;
			case 15:
				printf("F");
				break;
			default:
				if(x[b] < 10 && x[b] >= 0){
					printf("%d", x[b]);
				}
		}
	}
	printf("\n");
}

