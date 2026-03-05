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
