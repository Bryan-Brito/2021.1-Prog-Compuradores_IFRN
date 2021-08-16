programa
{ 
	 real a
      real b
      real c
      real x
	
	funcao inicio()
	{
	

         escreva ("Digite o valor do primeiro ângulo:")
         leia (a)

         escreva ("Digite o valor do segundo ângulo:")
         leia (b)

         escreva ("Digite o valor do terceiro ângulo:")
         leia (c)

         x = a + b + c

           se (x == 180) entao

             se (a == 90) ou (b == 90) ou (c = 90) entao
                escreva ("Seu triângulo é retângulo!")
             senao
                se (a < 90) e (b < 90) e (c < 90) entao
                   escreva ("Seu triângulo é acutângulo!")
                senao
                 escreva ("Seu triângulo é obtusângulo!")
                fimse
             fimse

           senao
             escreva ("Os valores apresentados não são válidos")
           fimse	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 325; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */