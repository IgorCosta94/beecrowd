#include<stdio.h>

int main(void){
	int a, n, total = 0;
	scanf("%d %d",&a,&n);
	
	if(n<=0){
		while(n<=0){
			scanf("%d",&n);
		}
	}
	
	for(int i =  a ; i >=0; i--){
		total += i;
	}
	for(int i =  n-1 ; i >=0; i--){
		total += i;		
	}
	printf("%d\n",total);
	return 0;
}
