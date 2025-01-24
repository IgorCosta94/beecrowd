#include<stdio.h>
#include<math.h>
int main(void){
	int n;
	scanf("%d",&n);
	
	if(n > 0 && n<= pow(10,6)){
		for(int a = 1; a <= n; a++){
			if(a < n){
				printf("Ho ");
			}
			else if(a == n){
				printf("Ho!\n");
			}
		}
	}
	return 0;
}
