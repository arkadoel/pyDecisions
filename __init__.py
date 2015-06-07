__author__ = 'arkadoel'
__first_version__ = '2015-jun-7'
import procesado

if __name__ == '__main__':


    frase = input('Escribe la pregunta: ')
    nombre = input('Escribe tu nombre: ')

    proceso = procesado.Procesa(frase, nombre)

    for c in range(0,5):
        proceso.hazlo()
