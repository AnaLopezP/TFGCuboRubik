

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
        uno = int(input("¿A qué posición va la posición 1? "))
        dos = int(input("¿A qué posición va la posición 2? "))
        tres = int(input("¿A qué posición va la posición 3? "))
        cuatro = int(input("¿A qué posición va la posición 4? "))
        ciclo = {1: uno, 2: dos, 3: tres, 4: cuatro}
        return ciclo
    
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
        nuevo_mov = []
        nuevo_mov.append(self.componer_ciclos(m1[0], m2[0]))
        nuevo_mov.append(self.componer_posiciones(m1[1], m2[1], m2[0]))
        nuevo_mov.append(self.componer_ciclos(m1[2], m2[2]))
        nuevo_mov.append(self.componer_posiciones(m1[3], m2[3]))
        print(m1[0][-1])
        
    def componer_ciclos(self, c1, c2):
        nuevo_ciclo = {}
        for i in range(len(c1)):
            valor = c1[i]
            valor2 = c2[valor]
            nuevo_ciclo[i] = valor2
        print(nuevo_ciclo)
        return nuevo_ciclo
    
    def componer_posiciones(self, p1, p2, c2):
        nueva_pos = []
        # se aplica la inversa de la permutación c2 a p1 y el resultado se suma a p2
        for i, j in c2.items():
            ciclo_inverso = {j: i}
            print(ciclo_inverso)
            # ordenar el ciclo inverso
            ciclo_inverso = dict(sorted(ciclo_inverso.items()))
            print(ciclo_inverso)
            # aplicar el ciclo inverso a p1
            pos = []
            for k in range(4):
                pos[c2[k]] = p1[k]
            print(pos)
            nueva_pos = [pos[i] + p2[i] for i in range(4)]
            print(nueva_pos)
            return nueva_pos

    
    
    
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