programa
{

  inteiro cont = 0
  inteiro i = 0
  inteiro numero = 1
  inteiro pares
  inteiro calculo
	
	funcao inicio()
	{
	enquanto(i < 10)
		{
		i = i + 1
		escreva("Digite o numero:")
		leia(numero)
		calculo = numero % 2

		se (calculo == 0) 
		{
			cont +=1		
			pares = numero
			escreva("O número ", pares," é Par", "\n")
		} 
		senao
		{
			escreva("O número não é Par", "\n")
		
		}
		}
		
			
			}	
				
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 414; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */