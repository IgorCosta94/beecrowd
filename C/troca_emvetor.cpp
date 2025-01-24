#include<stdio.h>
void inicializar(int *n);
void troca(int *n);
void exibicao(int *n);

int main(void){
	int n[20] ;
	inicializar(n);
	troca(n);
	exibicao(n);
	return 0;
}

void inicializar(int *n){
	int m;
	for(int a = 0; a<20;a++){
		scanf("%d", &m);
		n[a] = m;
	}
}

void troca(int *n){
	int x;
	int y = 19;
	for(int a = 0; a <=9; a++){
		x = n[a];
		n[a]=n[y];
		n[y] = x;
		y--;
	}
}

void exibicao(int *n){
	for(int w = 0; w < 20; w++){
		printf("N[%d] = %d\n", w ,n[w]);
	}
}
