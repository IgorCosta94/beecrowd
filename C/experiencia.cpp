#include<stdio.h>

int main(void){
	int n, quantia;
	int total = 0, total_c = 0, total_r = 0, total_s = 0;
	char cobaia;
	
	scanf("%d", &n);
	
	for(int w = 1; w <= n;){
		scanf("%d %c", &quantia, &cobaia);
		if(quantia >= 1 && quantia <= 15){
			w++;
			total += quantia;
			if(cobaia == 'C'){
				total_c += quantia;
			}
			if(cobaia == 'R'){
				total_r += quantia;
			}
			if(cobaia == 'S'){
				total_s += quantia;
			}
		}
	}
	printf("Total: %d cobaias\n", total);
	printf("Total de coelhos: %d\n", total_c);
	printf("Total de ratos: %d\n", total_r);
	printf("Total de sapos: %d\n", total_s);
	printf("Percentual de coelhos: %.2f %%\n", (total_c * 100.0) / total);
	printf("Percentual de ratos: %.2f %%\n", (total_r * 100.0) / total);
	printf("Percentual de sapos: %.2f %%\n", (total_s * 100.0) / total);
	return 0;
}
