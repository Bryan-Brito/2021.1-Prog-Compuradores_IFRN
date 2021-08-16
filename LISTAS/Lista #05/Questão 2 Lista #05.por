programa
{
	
	funcao inicio()
	{
		inteiro idade
		inteiro cont
		inteiro cont_sup
		
		escreva("Insira um número positivo")
		leia(idade)

		cont = 0
		cont_sup = 0
		enquanto (cont <= 10) {
				escreva("Insira um número positivo")
				leia(idade)
				cont = cont + 1
				se (idade >= 18) faca{
				   cont_sup = cont_sup + 1	
				}
				
		}
		
		escreva("Quantidade de pessoas maiores de idade:", cont_sup)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 348; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */