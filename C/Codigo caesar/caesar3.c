#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 128
//prototipo de funciones.
void encriptar(char frase[MAX],int numero);
void desencriptar(char frase[MAX],int numero);
 
//Función para desencriptar Cifrado Cesar en C
void desencriptar(char frase[MAX],int numero)
{
    int i=0;
    while(frase[i]!='\0')
    {
        frase[i]=frase[i]-numero;
        i++;
    }
    printf("\nLa frase desencriptada es:\n%s\n",frase);
}
//Función para encriptar Cifrado Cesar en C
void encriptar(char frase[MAX],int numero)
{
    int i=0;
    char letra;
    while(frase[i]!='\0')
    {
        frase[i]=frase[i]+numero;
        i++;
    }
    printf("\nLa frase encriptado es:\n%s\n",frase);
}
 
//Procedimiento principal.
int main()
{
    //Variables necesarias
    int x;
    char cadena[MAX];
	int characters = 0;//cantidad de caracteres
    int i = 1;//bucle caracteres
    int i2 = 1;//bucle []
    char c1 = 0;//caracter1
    //Presentación
   
    
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
    scanf("%128[^\n]", cadena);
    //Vacía el buffer del teclado
    while(getchar()!='\n');
    //Pedimos el número
    printf("introduce un numero : ");
    scanf("%d",&x);
    //Vacía el buffer del teclado
    while(getchar()!='\n');
    //Llamamos a la función encriptar
    encriptar(cadena, x);
    getchar();
    //Llamamos a la función desencriptar
    desencriptar(cadena, x);
    getchar();
    //Salimos
    return 0;
}
