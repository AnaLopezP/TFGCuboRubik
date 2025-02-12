

class LeyGrupo():
    def __init__(self, movimiento, nombre):
        self.movimiento = movimiento
        self.nombre = nombre
    
    
    def generar_movimiento(self):
        ciclo_alpha = self.crear_ciclo()
        pos_a = self.crear_posicion_arista()
        ciclo_beta = self.crear_ciclo()
        pos_b = self.crear_posicion_verice()
        self.movimiento = [ciclo_alpha, pos_a, ciclo_beta, pos_b]
        self.nombre = input("Ingrese el nombre (los giros) del movimiento: ")
        return self.movimiento
    '''Esta funcion genera un movimiento a partir de dos ciclos y dos posiciones'''
    
    def crear_ciclo(self):
        ciclo = []
        for i in range(4):
            rotacion = input("Ingrese 1, 2, 3, 4, o no conteste si no cambia de posición: ")
            if rotacion != "1" and rotacion != "2" and rotacion != "3" and rotacion != "4" and rotacion != "":
                print("Error: Ingrese 1, 2, 3, 4, o no conteste")
                return None
            if rotacion == "":
                return ciclo
            ciclo.append(rotacion)
        return ciclo
    ''' Esta funcion crea un ciclo a partir de las rotaciones que se le ingresen. En caso de que no se inserte un valor, se toma el ciclo por terminado'''
    
    def crear_posicion_arista(self):
        pos = []
        for i in range(4):
            color = input("Ingrese 0 o 1: ")
            if color != "0" and color != "1":
                print("Error: Ingrese 0 o 1")
                return None
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color de la arista está en su lugar (0) o no (1)'''

    def crear_posicion_verice(self):
        pos = []
        for i in range(4):
            color = input("Ingrese 0, 1 o 2: ")
            if color != "0" and color != "1" and color != "2":
                print("Error: Ingrese 0, 1, o 2")
                return None
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color del vertice está en su lugar (0), si está girado 1/3 a la izquierda (1) o 2/3 a la izquierda (2), mirándolo desde la esquina'''

    def __str__(self):
        return f"El movimiento {self.nombre} es: {self.movimiento}"
    
    
    def componer_movimientos(self, m1, m2):
        print(m1)
        print(m2)
        ciclo_alpha = []
        pos_a = []
        ciclo_beta = []
        pos_b = []
        print(m1[0][-1])
        
    
def main():
    movimiento1 = []
    nombre1 = ""
    ley = LeyGrupo(movimiento1, nombre1)
    movimiento1 = ley.generar_movimiento()
    print(ley)
    movimiento2 = []
    nombre2 = ""
    ley2 = LeyGrupo(movimiento2, nombre2)
    movimiento2 = ley2.generar_movimiento()
    print(ley2)
    print(movimiento1)
    print(movimiento2)

if __name__ == "__main__":
    main()