
'''
Pedir al usuario una cantidad en minutos y se mostrara en horas y minutos
'''

minutos = int(input('Cuantos son los minutos que desas transformar '))

horas = minutos // 60
minutos2 = minutos - (horas * 60)
print(f'Los {minutos} minutos en horas son: {horas}:{minutos2}')