# contador = 0
#while contador < 3:
#   entrada = input('Ingrese una palabra: ')
#    contador += 1
#    if entrada == 'Despedida':
#        print('Hasta luego!')
#        break
#else:
#    print('Se ha superado el numero maximo de intentos.')
#    print('Numero de intentos: ', contador)



    #while contador >= 3:
    #entrada = opciones_respuestas
    #contador += 1
    #if entrada == 'No se':
        #print('Salir')
        #break 
#else:
    #print('Se ha superado el numero maximo de intentos.')
    #print('Numero de intentos: ', contador)
entrada = " "

suma = 0

fallido = 0

while suma < 3:

    suma += 1

    print("Intento %d." % suma)

    entrada = input("Clave: ")

    print()

# Al ingresar "despedida", se evita que la variable fallido se incremente.

    if entrada == "despedida":

        continue

    fallido += 1

print("Tuviste %d intentos fallidos." % fallido)