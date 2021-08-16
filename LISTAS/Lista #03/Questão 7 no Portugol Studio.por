programa
{

	real  A, B, C, retangulo, obtusangulo


	funcao inicio()
	{
	escreva ("escreva o valor de A")
	leia (A)
	escreva ("escreva o valor de B ")
	leia(B)
	escreva ("escreva o valor de C")
	leia (C)
	
	se ((A > 0 e B >0 e C > 0) e (A + B + C == 180)) 
	{
 
	}
	se ((A == 90 ou B == 90 ou C == 90))
	{
		escreva("Seu triângulo é retângulo")
	}
	senao
	{
		se ((A > 90 ou B > 90 ou C > 90))
	{ 
		escreva("Seu triângulo é Obtusângulo")
	}
	senao
	{
		se ((A < 90 ou B < 90 ou C < 90) e ((A + B + C) == 180))
	{
		
		escreva ("Seu triângulo é acutângulo")
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
 * @POSICAO-CURSOR = 261; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */