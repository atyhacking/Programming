#include <stdio.h>
#include<stdbool.h>
#include<math.h>
#define MAX 128

/*
printf("");
scanf("%",&);
pritf("\n");
fflush(stdin);
*/

void encriptar(char frase[MAX],int numero)
{
    int i=0;
    char letra;
    while(frase[i]!='\0')
    {
        frase[i]=frase[i]+numero;
        i++;
    }
    printf("\nEncrypting...\n\n");
    printf("-> [ %d ]",frase);
}

int main()
{
    //VARIABLES
    int characters = 0;//cantidad de caracteres
    int i = 1;//bucle caracteres
    int i2 = 1;//bucle []
    char c1 = 0;//caracter1
    //char c2 = 0;//caracter2
   
    int y;
    char cadena[MAX];
    //CODIGO
    printf("How many characters? ");
    scanf("%d",&characters);
    printf("\n");
    fflush(stdin);
    //printf("\n");
    for(i=1;i<=characters;i++){
      	
        printf("Next character (%d/%d)? ",i,characters);
        scanf("%c",&c1);
        //scanf("%c",&c2);
        fflush(stdin);
        
    }
    printf("introduce un numero : ");
    scanf("%d",&y);
    //Vacía el buffer del teclado
    while(getchar()!='\n');
    //Llamamos a la función encriptar
    encriptar(cadena, y);
    getchar();
    
    /*
	for(i2=1;i2<=characters;i2++){
    	switch(x){
        	case 1:
        		printf("\n");
        		printf("Encrypting...");
        		printf("-> [ ");
        		printf("%c ",c1);
        		break;
        	case 2:
        		printf("%c ",c1);
        		break;
        	case 3:
        		printf("%c ",c1);
        		printf("]");
        		printf("\n");
        		break;
        	default:
        		printf("\n");
        		printf("NO PUEDE SER!!!");
        		return(0);
        		break;
		}
	}
    */

    return (0);
}
