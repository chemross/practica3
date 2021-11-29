import random
intentosRealizados = 0

número = random.randint(1, 100)

print('Bueno, estoy pensando en un número entre 1 y 100.')
while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimación = input()

    estimación = int(estimación)
    intentosRealizados = intentosRealizados + 1
    if estimación < número:

        print('Tu estimación es muy baja.')
    if estimación == número:

        break
if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
    
    