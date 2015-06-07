import random

class Procesa():
    '''
    clase para procesado de las ordenes
    '''
    def __init__(self, frase, nombre):
        self.frase =  str.lower(frase)
        self.nombre = str.lower(nombre)


    def generar_letras(self):
        abecedario = 'abcdefghijklmnñopqrstuvwxyz\'\" áéíóú¿?-+/%*.,;€$<>_¡!ºª@#()=[]{}'
        self.letras = {}

        for letra in abecedario:
            self.letras[letra] = random.randint(0,125)


    def tuercas(self):
        self.generar_letras()
        num_nombre = 0
        for letra in self.nombre:
            numero = self.letras[letra]
            num_nombre += numero
        #print('Nombre procesado --> ', num_nombre)
        num_frase = 0
        for letra in self.frase:
            nf = self.letras[letra]
            num_frase += nf
        #print('frase procesado --> ', num_frase)
        n1 = num_frase + num_nombre
        n2 = n1 * -1
        resultado1 = random.randrange(n2, n1)
        return resultado1

    def hazlo(self):
        print(' ')
        self.los_si = 0
        self.los_no = 0
        self.indeterminacion = 0

        for cont in range(1,4):
            resultado = self.tuercas()
            self.ver_resultado(Frase='Tirada ' + str(cont) + ': ', Valor=resultado)

        if self.los_no > self.los_si:
            print('\r\n\tTotal: No' )
        else:
            print('\r\n\tTotal: Si' )

    def ver_resultado(self, Frase=None, Valor=None):
        if Valor is 0:
            print(Frase, '--')
            self.indeterminacion +=1
        elif Valor%2 is 0:
            print(Frase, 'Sí')
            self.los_si += 1
        else:
            print(Frase, 'No')
            self.los_no += 1

