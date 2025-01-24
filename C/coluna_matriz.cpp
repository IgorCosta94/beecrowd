#include<stdio.h>

int main(void){
	float m[12][12];
	float valor,total = 0.0;
	int l;
	char t;
	scanf("%d", &l);
	scanf("%s", &t);
	
	for(int a = 0; a<12;a++){
		for(int b = 0; b<12;b++){
			scanf("%f", &valor);
			m[a][b]=valor;
		}
	}
	if(t == 'S'){
		for(int a = 0;a<12;a++){
			total += m[a][l];
		}
		printf("%.1f\n", total);
	}
	else if(t == 'M'){
		for(int a = 0;a<12;a++){
			total += m[a][l];
		}
		printf("%.1f\n", total/12);
	}

	return 0;
}
