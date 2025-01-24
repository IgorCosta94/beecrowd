#include<stdio.h>

void tomadas(void);

int main(void){
	tomadas();
	return 0;
}

void tomadas(void){
	int t1,t2,t3,t4;
	
	scanf("%d %d %d %d", &t1, &t2, &t3, &t4);
	printf("%d\n",(t1-1) + (t2-1) + (t3-1) + t4);
	
}
