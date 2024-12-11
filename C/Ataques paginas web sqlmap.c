#include<stdio.h>

/*
printf("");
scanf("%",&);
*/

int main(){
	
	int a = 0;
	
	printf("Inserte la url de la pagina weba a infectar: ");
	scanf("%d",&a);
	printf("\n");
	//paso 01
	do{
	
		sqlmap -u a --dbs;
	}
	
	
	return(0);
}
