def contar_letra_a(texto):
    count = 0
    for letra in texto:
        if letra == 'a' or letra == 'A':
            count += 1
    
    if count > 0:
        print(f'A letra \'a\' aparece {count} vezes na string.')
    else:
        print('A letra \'a\' não aparece na string.')
        
string = input("Digite uma string: ")
contar_letra_a(string)
