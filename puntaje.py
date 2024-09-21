questions = ('¿Un algoritmo es un conjunto de instrucciones secuenciales que permiten la resolución de un problema?', 
            ' Son ejemplos de lenguajes interpretados: Ruby, JavaScript y Python ',
            'En el ámbito de la informática, la identación cumple una función similar a la de la sangría en la escritura formal del lenguaje humano',
            '¿La identación es obligatoria en Python?',
            'Se encarga de ejecutar una misma acción “mientras que” una determinada condición se cumpla. ¿Lo anterior corresponde al bucle for?')

# Opciones de posibles respuestas 
options = (('A. True', 'B. False'),
            ('A. True', 'B. False'),
            ('A. True', 'B. False'),
            ('A. True', 'B. False'),
            ('A. True', 'B. False'))

#
answers = ('A', 'A', 'A', 'A', 'B' )
guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    # pedir al jugador que ingrese sus respeustas
    guess = input('Enter (A. True, B. False):').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECTO')
    else:
        print('INCORRECTO')
        print(f'{answers[question_num]} es la respuesta correcta')
    question_num += 1

    print('---------------------------------')
    print('            RESULTADOS           ')
    print('---------------------------------')

print('respuestas: ', end="")
for answer in answers:
    print(answer, end=" ")
print()

print('Preguntas: ', end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Mostrar puntaje final 
score = int(score / len(questions) * 100)
print(f'Tu puntaje es: {score}%')