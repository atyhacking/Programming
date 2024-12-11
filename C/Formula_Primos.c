#include<stdio.h>

int main(){
	int primer_numero = 3;
	int n = 0;
	int c = 0;//contador
	int r = 0;//resultat
	int d = 1;
	int den = 0;

	for(n=primer_numero;n<=200;n=n+2){
		
		for(c=3;c<=n;c=c+2){
			
			for(d=1;d<=n;d=d+2){
				r = n/c*d;
				den = c*d;
				if(r=1){
					if(((d=1)||(c=1))&&((d=n)||(c=n))){	
						printf("%d, ",n);
						c=n;
						d=n;
						break;
						
				 	}
					
				}
					
			}
			
			
			
			
		fflush(stdin);
		}
	}     
	
	      
	
	return(0);
}
