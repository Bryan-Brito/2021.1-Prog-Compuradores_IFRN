nome = "nome"
x = (3 + 1 >= ((16)**(1/2))) or (nome == "Miriam")
print(x)

profissao = "profissao"
x = (3 + 1 >= ((16)**(1/2))) and (profissao == "Advogado")
print(x)

Nome = "Nome"
x = (Nome != "Miriam") or (profissao == "Advogado") and (3 + 1 >= ((16)**(1/2)))
print(x)

teste = False
x = not teste and ((3 + 1) >= ((16) ** (1/2))) or not (profissao == "Advogado")
print(x)

x = not (((3 + 1) >= ((16) ** (1/2))) and teste)
print(x)