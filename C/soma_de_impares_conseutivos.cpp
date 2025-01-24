#include<stdio.h>

int main(void){
	int n,x,y,total=0;
	scanf("%d", &n);
	
	for(int w = 1; w <= n; w++){
		scanf("%d %d", &x,&y);
		if(x <= y){
			for(int a = x+1 ; a < y; a++){
				if(( a % 2 )== 1){
					total += a;
				}
			}
		}
		else if(x >= y){
			for(int a = y+1; a < x; a++){
				if(( a % 2 ) == 1){
					total += a;
				}
			}
		}
		printf("%d\n", total);
		total = 0;
	}
	return 0;
}
