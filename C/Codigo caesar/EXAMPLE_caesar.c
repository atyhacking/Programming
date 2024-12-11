#include<stdio.h>
#define LONG_MAX 30
void mayuscula(char *fraseOriginal_prt);
int cifrar(char *fraseOriginal_ptr,char *fraseConvertida_ptr,int clave);
int main(){
    char fraseOriginal[LONG_MAX];
    char fraseConvertida[LONG_MAX];
    int clave,opcion;
    printf("Cifrado de cesar");
    printf("\nCadena original:");
    fgets(fraseOriginal,LONG_MAX,stdin);
    mayuscula(fraseOriginal);//En este caso la misma cadena de entrada guardara los valores convertidos a mayuscula.
    printf("Ingrese clave:");
    scanf("%d", &clave);
    printf("Digite 1 para cifrar o 2 para descifrar:");
    scanf("%d",&opcion);
    printf("\nCadena mayuscula:%s",fraseOriginal);
    if(opcion == 1){
        cifrar(fraseOriginal,fraseConvertida,clave);
        printf("Cadena cifrada:%s",fraseConvertida);
  //  }else if(opcion == 2){
  //      descifrar(fraseOriginal,fraseConvertida,clave);
  //      printf("Cadena descifrada:%s",fraseConvertida);
    }else{
        printf("OPCION NO RECONOCIDA");
    }
    return 0;
}
 
void mayuscula(char *fraseOriginal_ptr){
while(*fraseOriginal_ptr){
    if(*fraseOriginal_ptr>='a' && *fraseOriginal_ptr<='z'){
        *fraseOriginal_ptr = *fraseOriginal_ptr-32;
    }
    fraseOriginal_ptr++;
}
return ;
}
 
int cifrar(char *fraseOriginal_ptr,char *fraseConvertida_ptr,int clave){
while(*fraseOriginal_ptr){
    if(*fraseOriginal_ptr>='a' && *fraseOriginal_ptr<='z'){
        *fraseOriginal_ptr = *fraseConvertida_ptr+clave;
    }
    fraseOriginal_ptr++;
}
while(*fraseConvertida_ptr){
    if(*fraseConvertida_ptr>='a' && *fraseConvertida_ptr<='z'){
        *fraseConvertida_ptr = *fraseConvertida_ptr-32;
    }
    fraseConvertida_ptr++;
}
return (0);
 
}
