#include<stdio.h>

int main(void){
	int i = 1;
	for( int j = 60 ; j >= 0 ; j -= 5 ,i += 3){
		printf("I=%d J=%d\n", i ,j);
	}

	return 0;
}
