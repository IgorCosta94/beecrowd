#include<stdio.h>

int main(void){
	int  gol_i, gol_g;
	int grenal = 0, v_inter = 0, v_gremio = 0, empate = 0, cont_grenal = 0;
	
	while(grenal != 2){
		scanf("%d %d", &gol_i,&gol_g);
		printf("Novo grenal (1-sim 2-nao)\n");
		scanf("%d", &grenal);
		cont_grenal++;
		
		if(gol_i > gol_g){
			v_inter++;
		}
		else{
			v_gremio++;
		}
		if(gol_i == gol_g){
			empate++;
		}
	}
printf("%d grenais\n",cont_grenal);
printf("Inter:%d\n",v_inter);	
printf("Gremio:%d\n",v_gremio);	
printf("Empate:%d\n",empates);
v_inter > v_gremio ? printf("Inter venceu mais\n"):printf("Gremio venceu mais\n");
	return 0 ;
}
