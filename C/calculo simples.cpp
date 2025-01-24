#include <stdio.h>
 
int main(void) {
	int codigo, quan_peca, codigo1, quan_peca1;
	float valor, valor1;
	
    scanf("%d%d%f", &codigo,&quan_peca,&valor);
    scanf("%d%d%f", &codigo1,&quan_peca1,&valor1);
    
	printf("VALOR A PAGAR: R$ %.2f", quan_peca * valor + quan_peca1 * valor1 );
 
    return 0;
}
