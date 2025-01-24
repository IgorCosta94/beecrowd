#include<stdio.h>

int main(void){
	float salario, novo_salario, reajuste;
	scanf("%f", &salario);
	
	if(salario > 0 && salario <= 400.00){
		reajuste = salario * 0.15;
		novo_salario = salario + reajuste;
		printf("Novo salario: %.2f\n", novo_salario);
		printf("Reajuste ganho: %.2f\n", reajuste);
		printf("Em percentual: 15 %%");
	}
	else	if(salario >= 400.01 && salario <= 800.00){
				reajuste = salario * 0.12;
				novo_salario = salario + reajuste;
				printf("Novo salario: %.2f\n", novo_salario);
				printf("Reajuste ganho: %.2f\n", reajuste);
				printf("Em percentual: 12 %%");
	}
	else	if(salario >= 800.01 && salario <= 1200.00){
				reajuste = salario * 0.10;
				novo_salario = salario + reajuste;
				printf("Novo salario: %.2f\n", novo_salario);
				printf("Reajuste ganho: %.2f\n", reajuste);
				printf("Em percentual: 10 %%");
	}
	else	if(salario >= 1200.01 && salario <= 2000.00){
				reajuste = salario * 0.07;
				novo_salario = salario + reajuste;
				printf("Novo salario: %.2f\n", novo_salario);
				printf("Reajuste ganho: %.2f\n", reajuste);
				printf("Em percentual: 7 %%");
	}
	else	if(salario > 2000.00){
				reajuste = salario * 0.04;
				novo_salario = salario + reajuste;
				printf("Novo salario: %.2f\n", novo_salario);
				printf("Reajuste ganho: %.2f\n", reajuste);
				printf("Em percentual: 4 %%");
	}	
	return 0;
}
