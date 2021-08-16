programa
{
real  a, b, c
	
	funcao inicio()
	{
      escreva ("digite o lado de  A")
	 leia (a)
	 escreva ("digite o lado de B")
	 leia(b)
	 escreva ("digite o lado de C")
	 leia (c)
		se ((a > 0 e b > 0 e c > 0) e (a > c - b) ou (a < b + c) e (b > a - c) ou (b < a + c) e (c > a - b) ou (c < a + b))
		
	{
		escreva ("é um triângulo")	
			
			}
          se ((a == b e b == c) e (a > 0 e b > 0 e c > 0))
			{  
				escreva ("Seu triângulo é equilátero")
				
				}
				senao { 
					
					se ((a != b e b!= c) e (a > 0 e b > 0 e c > 0))
					{
						escreva ("Seu triângulo é escaleno")
					}
					senao {	

						se (((a == b e b != c) ou (b == a e a!=c) ou (b == c e c!=a) ou (c == a e a!=b) ou (c == b e b!=a)) e (a > 0 e b > 0 e c > 0))
					
					{
						escreva("Seu triângulo é isósceles")						
						}
						senao
				{
					escreva("Não foi possível calcular")
				}
					}
		}
	
}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 870; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */