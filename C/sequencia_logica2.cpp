#include<stdio.h>

int main(void){
	int x, y,b=1;
	scanf("%d %d", &x, &y);
	
	for(int a = 1; a <= y;a++){
		if(b<x){
			printf("%d ",a);
		}
		else if(b == x){
			printf("%d\n",a);
			b = 0;
		}
		b++;
	}
	return 0;
}
