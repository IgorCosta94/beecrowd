#include<stdio.h>

int main(void){
	int n,x,y;
	int cont = 1;
	scanf("%d", &n);
	
	while(cont <= n){
		scanf("%d %d", &x, &y);
		if(y == 0){
			printf("Divisao impossivel\n");
		}
		else{
			printf("%.1f\n", (x*1.0)/y);
		}
		cont++;
	}
	return 0;
}
