#include<stdio.h>

int main(void){
	int n,x,y;
	int total, cont, cont2=1;
	
	scanf("%d", &n);
	
	while(cont2<=n){
		scanf("%d %d", &x, &y);
		total = 0;
		cont =1;
		while(cont <= y){
			if(x % 2 == 0 || x % 2 == -1){
				total += x;
				cont += 1;
			}
			x +=1;
		}
		printf("%d\n",total);
		cont2 += 1;
	}
	return 0;
}

/*1233
1231
1520289
Erro40000
Erro1
25
8
15

1233
1231
1520289
correto 36000
correto -19
25
8
15*/
