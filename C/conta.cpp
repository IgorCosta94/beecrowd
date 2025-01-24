#include<stdio.h>

int main(void){
	int n,m;
	int a1,a2, soma;
	a1=1;a2=1;
	scanf("%d",&n);
	for(int x = 0;x < n;x++){
		scanf("%d",&m);
		soma = 0;
		for(int w = 0;w<m;w++){
			if(w%2==0){
				soma += a1;
			}
			else if(w%2==1){
				soma += -a2;
			}
		}
		printf("%d\n",soma);
	}

	return 0;
}
