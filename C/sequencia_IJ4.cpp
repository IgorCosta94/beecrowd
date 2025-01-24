#include<stdio.h>

int main(void){
	float i = 0.0;
	float j = 1.0;
	int cont = 0;

	for( float w = 0.0 ; w <= 3.0 ; ){
		if(cont == 3){
			w += 0.2;
			j = 1;
			j += w;
			cont = 0;
		}
		cont +=1;
		
		if(w == 0.0 || w== 1.0){
			printf("I=%.0f J=%.0f\n", w,j++);
		}
		else if(w >= 0.2 && w <= 0.8){
			printf("I=%.1f J=%.1f\n", w,j++);
		}
		else if(w >= 1.2 && w <= 1.8){
			printf("I=%.1f J=%.1f\n", w,j++);
		}
		else if(w >= 2.0 && w <= 2.2){
			printf("I=%.0f J=%.0f\n", w,j++);
		}
		
	}

	return 0;
}
