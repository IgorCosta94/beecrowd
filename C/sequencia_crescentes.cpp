#include<stdio.h>

int main(void){
	int x;
	scanf("%d", &x);
	
	while(x > 0){
		for(int a = 1; a <= x; a++){
			if(a<x){
				printf("%d ",a);
			}
			else if(a==x){
				printf("%d\n",a);
			}
		}
		scanf("%d", &x);	
	}
	
	return 0;
}
