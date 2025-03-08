import csv

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
        if not self.comprobar_restricciones(self.movimiento):
            print("Error: No se cumplieron las restricciones.")
            return None
        return self.movimiento
    '''Esta funcion genera un movimiento a partir de dos ciclos y dos posiciones'''
    
    def crear_ciclo(self):
        #ciclo = []
        uno = int(input("¿A qué posición va la posición 1? "))
        dos = int(input("¿A qué posición va la posición 2? "))
        tres = int(input("¿A qué posición va la posición 3? "))
        cuatro = int(input("¿A qué posición va la posición 4? "))
        ciclo = {1: uno, 2: dos, 3: tres, 4: cuatro}
        return ciclo
    
    def crear_posicion_arista(self):
        pos = []
        for i in range(4):
            color = int(input("Ingrese 0 o 1: "))
            if color != 0 and color != 1:
                print("Error: Ingrese 0 o 1")
                return None
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color de la arista está en su lugar (0) o no (1)'''

    def crear_posicion_verice(self):
        pos = []
        for i in range(4):
            color = int(input("Ingrese 0, 1 o 2: "))
            if color != 0 and color != 1 and color != 2:
                print("Error: Ingrese 0, 1, o 2")
                break
            pos.append(color)
            i += 1
        return pos
    '''Esta funcion indica si el color del vertice está en su lugar (0), si está girado 1/3 a la izquierda (1) o 2/3 a la izquierda (2), mirándolo desde la esquina'''
    
    def guardar_en_csv(self, archivo_csv):
        """Guarda el movimiento actual en un archivo CSV"""
        if self.movimiento and self.nombre:
            with open(archivo_csv, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.nombre, self.movimiento])
            print(f"Movimiento {self.nombre} guardado en {archivo_csv}")
        else:
            print("No hay movimiento generado para guardar.")

    '''@staticmethod
    def cargar_desde_csv(archivo_csv):
        """Carga los movimientos desde un archivo CSV"""
        movimientos = []
        try:
            with open(archivo_csv, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    nombre = row[0]
                    perm_aristas = eval(row[1])  
                    colores_aristas = eval(row[2])  
                    perm_vertices = eval(row[3])
                    colores_vertices = eval(row[4])
                    movimientos.append((nombre, [perm_aristas, colores_aristas, perm_vertices, colores_vertices]))
        except FileNotFoundError:
            print("No se encontró el archivo CSV.")
        return movimientos'''

    def __str__(self):
        return f"El movimiento {self.nombre} es: {self.movimiento}"
    
    def componer_movimientos(self, m1, m2):
        print(m1)
        print(m2)
        nuevo_mov = []
        nuevo_mov.append(self.componer_ciclos(m1[0], m2[0]))
        nuevo_mov.append(self.componer_posiciones_mod2(m1[1], m2[1], m2[0]))
        nuevo_mov.append(self.componer_ciclos(m1[2], m2[2]))
        nuevo_mov.append(self.componer_posiciones_mod3(m1[3], m2[3], m2[2]))
        #print(nuevo_mov)
        return nuevo_mov
        
    def componer_ciclos(self, c1, c2):
        nuevo_ciclo = {}
        for i in range(len(c1)):
            valor = c1[i+1]
            valor2 = c2[valor]
            nuevo_ciclo[i+1] = valor2
        #print(nuevo_ciclo)
        return nuevo_ciclo
    
    def calcular_ciclo_inverso(self, c2):
        ciclo_inverso = {j: i for i, j in c2.items()}  # Generar inversa
        return dict(sorted(ciclo_inverso.items()))  # Ordenarlo
    
    def componer_posiciones_mod2(self, p1, p2, c2):
        ciclo_inverso = self.calcular_ciclo_inverso(c2)
        #print("Ciclo inverso:", ciclo_inverso)

        pos = [0] * 4
        for k in range(4):
            x = ciclo_inverso[k+1]
            pos[k] = p1[x-1]
        #print("Pos mod 2:", pos)

        nueva_pos = [(pos[i] + p2[i]) % 2 for i in range(4)]
        #print("Nueva posición mod 2:", nueva_pos)
        return nueva_pos

    def componer_posiciones_mod3(self, p1, p2, c2):
        ciclo_inverso = self.calcular_ciclo_inverso(c2)
        #print("Ciclo inverso:", ciclo_inverso)

        pos = [0] * 4
        for k in range(4):
            x = ciclo_inverso[k+1]
            pos[k] = p1[x-1]
        #print("Pos mod 3:", pos)

        nueva_pos = [(pos[i] + p2[i]) % 3 for i in range(4)]
        #print("Nueva posición mod 3:", nueva_pos)
        return nueva_pos
    
    def comprobar_restricciones(self, m1):
        # primero comprobamos que el sumatorio de las posiciones de las aristas sea cero
        if sum(m1[1]) % 2 != 0:
            return False
        # luego comprobamos que el sumatorio de las posiciones de los vertices sea cero
        if sum(m1[3]) % 3 != 0:
            return False
        # por último comprobamos que la composicion de los ciclos sea la identidad
        identidad = self.componer_ciclos(m1[0], m1[2])
        if identidad != {1: 1, 2: 2, 3: 3, 4: 4}:  # si no es la identidad
            return False
        else:
            return True
        
    def comparar_movimientos(self, m1, m2):
        if m1 == m2:
            return True
        else:
            return False
        

    
    
# creamos un csv con los movimientos base de datos (son 34) solo si no existe
def crear_csv():
    while True:
        print("-------------------- GENERANDO MOVIMIENTO --------------------")
        mov = LeyGrupo([], "")
        mov.generar_movimiento()
        mov.guardar_en_csv("movimientos.csv")
        
        continuar = input("¿Desea continuar? (s/n): ").strip().lower()
        if continuar != "s":
            break
        
'''# cargamos los movimientos del csv
movimientos = LeyGrupo.cargar_desde_csv("movimientos.csv")
print("Movimientos cargados:")
for nombre, movimiento in movimientos:
    print(f"{nombre}: {movimiento}")
    '''
    
# creamos una clase Nodo para almacenar los movimientos
class Nodo():
    def __init__(self, numero, nombre, movimiento):
        self.numero = numero
        self.nombre = nombre
        self.movimiento = movimiento
        self.adyacentes = []
    
    def agregar_adyacente(self, nodo):
        self.adyacentes.append(nodo)
    
    def __str__(self):
        return f"El movimiento es: {self.movimiento}"    

# creamos un grafo con los movimientos del csv
class Grafo():
    def __init__(self):
        self.nodos = {} # diccionario {numero del nodo: nodo}
    
    def agregar_nodo(self, numero, nombre, movimiento):
        if numero not in self.nodos:
            self.nodos[numero] = Nodo(numero, nombre, movimiento)
        else:
            print("Ya existe un nodo con ese número.")
    
    def agregar_arista(self, numero1, numero2):
        if numero1 in self.nodos and numero2 in self.nodos:
            self.nodos[numero1].agregar_adyacente(self.nodos[numero2])
            self.nodos[numero2].agregar_adyacente(self.nodos[numero1])
        else:
            print("Al menos uno de los nodos no existe.")
    
    def mostrar_grafo(self):
        for num, nodo in self.nodos.items():
            print(f"Nodo {num} ({nodo.movimiento}): {[n.numero for n in nodo.adyacentes]}")
            
    def expandir_grafo(self):
        lg = LeyGrupo([], "")
        nuevos_nodos = []
        for num1, nodo1 in self.nodos.items():
            for num2, nodo2 in self.nodos.items():
                if num1 != num2:
                    nuevo_mov = lg.componer_movimientos(nodo1.movimiento, nodo2.movimiento)
                    if not any(lg.comparar_movimientos(nuevo_mov, nodo.movimiento) for nodo in self.nodos.values()):
                        nuevo_num = max(self.nodos.keys()) + 1
                        self.agregar_nodo(nuevo_num, f"{nodo1.nombre}{nodo2.nombre}", nuevo_mov)
                        nuevos_nodos.append(nuevo_mov)
                        self.agregar_arista(num1, nuevo_num)
                        self.agregar_arista(num2, nuevo_num)
                    else:
                        nodo_existente = next(n for n in self.nodos.values() if lg.comparar_movimientos(nuevo_mov, n.movimiento))
                        self.agregar_arista(nodo1.numero, nodo_existente.numero)
        return nuevos_nodos
    
    def guardar_grafo_csv(self, archivo_csv):
        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for nodo in self.nodos.values():
                writer.writerow([nodo.numero, nodo.nombre, nodo.movimiento])
            print(f"Grafo guardado en {archivo_csv}")

#cargo los movimientos del csv
grafo = Grafo()
with open("movimientos.csv",newline= "", mode='r', encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        nombre = row[0]
        movimiento = eval(row[1])
        grafo.agregar_nodo(i, nombre, movimiento)
        
grafo.expandir_grafo()
grafo.mostrar_grafo()
grafo.guardar_grafo_csv("grafo.csv")

# componemos los movimientos y hay que comparar el nuevo movimiento con los que ya tenemos. si no existe, lo agregamos con un nuevo numero