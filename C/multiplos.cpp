#include<stdio.h>

int main(void){
	int w, x;
	scanf("%d%d", &w, &x);
	if(x>w){
	
		x % w == 0 ? printf("Sao Multiplos\n") : printf("Nao sao Multiplos\n");
	}
	else{
		w % x == 0 ? printf("Sao Multiplos\n") : printf("Nao sao Multiplos\n");
	}
	return 0;
}
