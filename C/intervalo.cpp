#include<stdio.h>

int main(void){
	float n;
	scanf("%f",&n);
	
	if(n > 25.00 && n <= 50.00){
		printf("Intervalo (25,50]");
	}
	else if(n >= 0.00 && n <= 25.00){
		printf("Intervalo [0,25]");
	}
	else if(n >= 75.00 && n <= 100.00){
		printf("Intervalo (75,100]");
	}
	else{
		printf("Fora de intervalo");
	}
	
	return 0;
}
