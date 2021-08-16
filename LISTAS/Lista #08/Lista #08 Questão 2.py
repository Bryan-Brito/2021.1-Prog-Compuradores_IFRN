str_input = 'Bruce Wayne;8;5,75#Clark Kent;5,71;4,1#Diana Prince;1.85;0,5'

str_input = str_input.split('#')

direc = [[],[],[]]
media = 0
for i in range(len(direc)):
    direc[i].append(str_input[i])
    print(direc)
for i in range(0, len(direc)):
    n1 = direc[i][1]
    n2 = direc[i][2]
    media = n1 + n2
    direc.insert([3],media)
    media = 0
    print(direc)
    print(media)