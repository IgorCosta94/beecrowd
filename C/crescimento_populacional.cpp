#include<stdio.h>

int main(void){
	int pa, pb,t;
	int cont2 = 1, cont = 0;
	double g1, g2;
	
	scanf("%d", &t);
	while(cont2 <= t){
		cont = 0;
		scanf("%d %d %lf %lf", &pa, &pb, &g1, &g2);
		while(pb >= pa ){
            pa += int(pa * (g1/100));
            pb += int(pb * (g2/100));
			cont++;
			if(cont > 100) break;			
		}
		if(cont > 100){
			printf("Mais de 1 seculo.\n");
		}
		else{
			printf("%d anos.\n",cont);
		}
			
		cont2++;
	}
	
	return 0;
}
