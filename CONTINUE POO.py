'''
TAREA CONTINUE POO
Crea un programa en Python que simule el procesamiento de una lista de datos numéricos utilizando programación orientada a objetos. 
El programa debe definir una clase llamada Procesador que contenga un método procesar. Este método debe iterar a través de la lista de datos y aplicar las siguientes reglas:
    • Si un número en la lista es igual a 3, el procesamiento de ese número debe ser saltado utilizando la instrucción continue.
    • Si un número en la lista es igual a 5, el procesamiento debe detenerse por completo utilizando la instrucción break.
    • Para cualquier otro número, el programa debe imprimir un mensaje indicando que el número está siendo procesado.
El programa debe crear una instancia de la clase Procesador con una lista de ejemplo y llamar al método procesar para demostrar el funcionamiento del código.
'''
class Procesador:
    def procesar(self, lista_datos):
        for i in lista_datos:
            if i == 3:
                continue
            elif i == 5:
                break
            else:
                print(f"El número {i} está siendo procesado...")    
mi_procesador = Procesador()
lista_datos = [1,2,3,4,5,6] 
mi_procesador.procesar(lista_datos)
