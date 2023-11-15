altura = int(input("medida da altura: "))
largura = int(input("medida da largura: "))
ab = "a"

if altura == 1:
    print(ab * (largura))

elif largura == 1:
    for c in range(altura):
        print(ab)
elif altura < 0 or largura <0:
    print()

else:
    print(ab * largura)
    for b in range(altura - 2):
        print(ab + " " *(largura -2)+ ab)
        '''
        printa o primeiro, espaços em branco -2(correspondendo ao 
        primeiro e o útltimo) e o último a
        '''

    print(ab * largura)
