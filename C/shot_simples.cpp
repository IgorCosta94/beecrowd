#include<stdio.h>

int main(void){
	int a, b, c, d;
	scanf("%d%d%d", &a, &b, &c );
	
	if(a > b && a > c){
		d = a;
		if(b > c){
			a = c;
			c = d;
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",c,b,a);
		}
		else if(b < c){
			a = b;
			b = c;
			c = d;
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",c,a,b);
		}
	}
	else if(b > a && b > c){
		d = b;
		if(a > c){
			b = a;
			a = c;
			c = d;
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",b,c,a);
		}
		else if(a < c){
			b = c;
			c = d;
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",a,c,b);
		}
	}
	else if(c > a && c > b){
		if(a > b){
			d = a;
			a = b;
			b = d;
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",b,a,c);
		}
		else if(a < b){
			printf("%d\n%d\n%d\n\n",a,b,c);
			printf("%d\n%d\n%d\n",a,b,c);
		}
	}
	return 0;
}
