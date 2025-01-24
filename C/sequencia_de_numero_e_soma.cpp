#include<stdio.h>

int main(void){
	int m,n,total=0;
	
	scanf("%d %d", &m,&n);
	
	while(m > 0 && n > 0){
		if(n < m){
			for(int w = n; w <= m; w++){
				printf("%d ",w);
				total += w;
			}
			printf("Sum=%d\n",total);
		}
		else if(m < n){
			for(int w = m; w <= n; w++){
				printf("%d ",w);
				total += w;
			}
			printf("Sum=%d\n",total);
		}
		total = 0;
		scanf("%d %d", &m,&n);
	}
	
	return 0;
}
