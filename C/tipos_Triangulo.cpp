#include<stdio.h>
#include<math.h>

void ordem();
void triangulo(float a, float b, float c);

int main(void){
	ordem();
	return 0;
}

void ordem(){
	float a, b, c, d;
	scanf("%f%f%f", &a, &b, &c);
	
	if(a >= b && a >= c){
		if(b <= c){
			d = b;
			b = c;
			c = d;
		}
		else if(b>=a){
			a = a;
			b = b;
			c = c;
		}
	}
	else if(b >= a && b >= c){
		d = b;
		if(a >= c){
			b = a;
			a = d;
		}
		else if(a <= c){
			b = c;
			c = a;
			a = d;
		}
	}
	else if(c >= a && c >= b){
		d = c;
		if(a >= b){
			c = b;
			b = a;
			a = d;
		}
		else if(a <= b){
			c = a;
			a = d;
		}
	}
	triangulo(a,b,c);
}

void triangulo(float a, float b, float c){
	if(a >= b + c){
		printf("NAO FORMA TRIANGULO\n");
		return;
	}

	if(pow(a, 2) == pow(b, 2) + pow(c, 2)){
		printf("TRIANGULO RETANGULO\n");
	}
	if(pow(a, 2) > pow(b,2) + pow(c,2)){
		printf("TRIANGULO OBTUSANGULO\n");
	}
	if(pow(a, 2) < pow(b, 2) + pow(c, 2)){
		printf("TRIANGULO ACUTANGULO\n");
	}
	if(a == b && b == c){
		printf("TRIANGULO EQUILATERO\n");
	}                
	else if( a == b || a == c || b == c ){
		printf("TRIANGULO ISOSCELES\n");
	}
	
}


