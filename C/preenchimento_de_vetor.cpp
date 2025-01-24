#include<stdio.h>

int main(void){
	int n[10];
	int a;
	scanf("%d", &a);
	n[0] = a;
	printf("N[0] = %d\n", n[0]);
	for(int x = 1 ; x < 10; x++){
		n[x] = n[x - 1] * 2;
		printf("N[%d] = %d\n",x , n[x]);
	}
	return 0;
}
