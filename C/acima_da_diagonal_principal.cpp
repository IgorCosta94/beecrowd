#include<stdio.h>

int main(void){
	float m[12][12];
	float valor;
	double total = 0.0;
	int cont;
	char t;
	
	scanf("%s", &t);
	
	for(int a = 0; a<12;a++){
		for(int b = 0; b<12;b++){
			//scanf("%f", &valor);
			m[a][b]=10;
	
		}
		
	}
	if(t == 'S'){
		cont=1;
		for(int a = 0;a<12;a++){
			for(int b =1 ;b < cont ;b++){
				total += m[a][b];	
			}
			cont++;
		}
		printf("%.1lf\n", total);
	}
	else if(t == 'M'){
		cont=1;
		for(int a = 0;a<12;a++){
			for(int b =1 ;b < cont ;b++){
				total += m[a][b];
			}
			cont++;
		}
		printf("%.1lf\n", total/66.0);
	}

	return 0;
}
