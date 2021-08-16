palavra = input('Insira uma palavra: ')

cont = []
for i in range(len(palavra)):
    if ('A' == palavra[i] or 'a' == palavra[i] or 'E' == palavra[i]or 'e' == palavra[i] or 'I' == palavra[i] or 'i' == palavra[i] or 'O' == palavra[i] or 'o' == palavra[i] or 'U' == palavra[i] or 'u' == palavra[i]):
        cont.append(palavra[i])
    if ('Á' == palavra[i] or 'á' == palavra[i] or 'É' == palavra[i]or 'é' == palavra[i] or 'Í' == palavra[i] or 'í' == palavra[i] or 'Ó' == palavra[i] or 'ó' == palavra[i] or 'Ú' == palavra[i] or 'ú' == palavra[i]):
        cont.append(palavra[i])
    if ('Â' == palavra[i] or 'â' == palavra[i] or 'Ê' == palavra[i]or 'ê' == palavra[i] or 'Î' == palavra[i] or 'î' == palavra[i] or 'Ô' == palavra[i] or 'ô' == palavra[i] or 'Û' == palavra[i] or 'û' == palavra[i]):
        cont.append(palavra[i])
    if ('Ã' == palavra[i] or 'ã' == palavra[i] or 'Ẽ' == palavra[i]or 'ẽ' == palavra[i] or 'Ĩ' == palavra[i] or 'ĩ' == palavra[i] or 'Õ' == palavra[i] or 'õ' == palavra[i] or 'Ũ' == palavra[i] or 'ũ' == palavra[i]):
        cont.append(palavra[i])
    if ('À' == palavra[i] or 'à' == palavra[i] or 'È' == palavra[i]or 'è' == palavra[i] or 'Ì' == palavra[i] or 'ì' == palavra[i] or 'Ò' == palavra[i] or 'ò' == palavra[i] or 'Ù' == palavra[i] or 'ù' == palavra[i]):
        cont.append(palavra[i])

print("Vogais da palavra '{0}': {1}".format(palavra, cont))