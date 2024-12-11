#include<stdio.h>
#include<stdbool.h>

/*
printf("");
scanf("%",&);
printf("\n");
fflush(stdin);
*/

int main(){
	int c = 0;
	int c1 = 0;
	int c2 = 0;
	bool b = true;
	
	printf("PRINTEO");
	while(b == true){
		printf("CREACION DE UNA NUEVA PASSWORD\n");
		printf("Password: ");
		scanf("%d1",&c1);
		printf("\n");
		//fflush(stdin);
		printf("Repita su password: ");
		scanf("%d",&c2);
		printf("\n");
		//fflush(stdin);
		if(c1==c2){
			printf("Password guardada");
			b = false;
		}else{
			printf("Las passwords no coinciden, repita de nuevo: \n\n");
			//fflush(stdin);
			b = true;
		}
		
	}
	
	return(0);
}
