#include<stdio.h>
#include<string.h>
int main(void){
	char par[]="PAR";
	char impar[]="IMPAR";
	char nome1[100];
	char nome2[100];
	char escolha1[10];
	char escolha2[10];
	int qt,n1,n2;
	scanf("%d",&qt);
	while(qt > 0){
		scanf("%s %s %s %s", nome1, escolha1, nome2, escolha2);
		scanf("%d %d", &n1, &n2);
		if( ((n1+n2)%2 ) == 0 ){
			if((strcmp(escolha1,par) )==0 ){
				printf("%s\n", nome1);
			}
			else{
				printf("%s\n", nome2);
			}
		}
		else{
			if((strcmp(escolha2,impar) )==0 ){
				printf("%s\n", nome2);
			}
			else{
				printf("%s\n", nome1);
			}
			
		}
		qt--;
	}
	return 0;
}
