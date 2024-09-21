# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: 

#Modulo random (paso 4)
import random 
print('¡Te doy la bienvenida a la Trivia sobre Python!')
# Paso 3
# Nombre usuario
nombre = input('Ingresa tu nombre, por favor: ')
# Edad usuario
edad = int(input('Ingresa tu edad, por favor: '))

if edad >= 18:
    print(f' \n¡Hola {nombre}, Es hora de comenzar con la Trivia sobre python!\n ')
    print('Antes de comenzar, las instrucciones del juego son las siguientes: ')
    print('debes de contestar correctamente las preguntas, por cada respuesta correcta \nvas a ganar 1 punto. Sin emabrgo, por cada respuesta incorrecta \nno sumaras puntos, pero si te equivocas más de tres veces pierdes el juego.')
    print('¡Ahora si, a jugar!')
    print('------------------------------------')
else:
    print(f'Lo siento {nombre}, no tienes la edad mínima para jugar. ')
    exit()

# Paso 5 preguntas y respuestas
# Definir las preguntas y sus respuestas en un diccionario
preguntas = [
    ('¿Un algoritmo es un conjunto de instrucciones secuenciales que permiten la resolución de un problema?'), 
    ('Son ejemplos de lenguajes interpretados: Ruby, JavaScript y Python'),
    ('En el ámbito de la informática, la identación cumple una función similar a la de la sangría en la escritura formal del lenguaje humano'),
    ('¿La identación es obligatoria en Python? '),
    ('Se encarga de ejecutar una misma acción “mientras que” una determinada condición se cumpla. ¿Lo anterior corresponde al bucle for?')] # FALTA AÑADIR LAS PREGUNTAS!

# Opciones de posibles respuestas 
opciones_respuestas = (('A.Verdadero', 'B.Falso'),
                    ('A.Verdadero', 'B.Falso'),
                    ('A.Verdadero', 'B.Falso'),
                    ('A.Verdadero', 'B.Falso'),
                    ('A.Verdadero', 'B.Falso'))

# Definimos las respuestas correctas
respuestas = ('A', 'A', 'A', 'A', 'B') # NO ESTOY SEGURA DE ESTE
numero_pregunta = 0
# Usar shuffle para mezclar las preguntas 
random.shuffle(preguntas)

# Puntaje
score = 0
aciertos = []
contador_errores = 0 # FALTA AGREGAR ESTOOOOO
# Recorrer cada pregunta
for pregunta in preguntas: 
    print('-----------------------------------')
    print(pregunta)
    for opcion in opciones_respuestas[numero_pregunta]:
        print(opcion)

#Obtener la respuesta del usuario y mostrar si es correcta o incorrecta
    acierta = input('Responde (A o B): ').upper()
    aciertos.append(acierta)
    if acierta == respuestas[numero_pregunta]:
        score += 1
        print('Respuesta correcta')
        
    else: 
        print('Respuesta incorrecta')
        print(f'{respuestas[numero_pregunta]} es la respuesta correcta')
    numero_pregunta += 1

# Mensaje para separar y mostrar los resultados
print('---------------------------------')
print('            RESULTADOS           ')
print('---------------------------------')

# Mostrar las respuestas correctas al jugador
print('Respuestas correctas: ', end="")
for respuesta in respuestas:
    print(respuesta, end=" ")
print()

# Mostrar las respuestas que coloco el jugador
print('Respuestas del jugador: ', end="")
for acierta in aciertos:
    print(acierta, end=" ")
print()

# FALTA CONTADOR DE ERRORES!!!!!!!!!!!!!!!!

# Mostrar puntaje final
score = int(score / len(preguntas) * 100)
print(f'Tu puntaje es: {score}%')

# Mostrar mensaje final
print('\n¡Gracias por jugar esta trivia sobre Python, bonito día!')