#Reto # 7 - Julio Cesar Palacio Ojeda - Grupo 23 - 01/06/2022
#Aplicación para registrar los datos de los estudiantes que se postulan al departamento de 
#prácticas académicas de una de las universidades extranjeras.
#Datos de Entrada: archivo de texto: 'codigos_estudiantes.txt' enviada por el departamento de prácticas académica de la universidad
#Profesor la prueba unitaria por favor verla en el archivo adjunto pueba_unitaria tambien adjunto los pantallazos de la prueba en pdf.
#Se importa la libreria networkx como nx
import networkx as nx
import funciones as fun
#Se importa la libreria pyplot de matplotlib como plt
import matplotlib.pyplot as plt
import datetime

#Inicializamos lista de postulados (leyendo el archivo de texto: 'codigos_estudiantes.txt' enviada por el departamento de prácticas académica de la universidad)
lista_postu = []

for i in fun.leer_archivos():
  lista_postu.append(i)
  
#Inicializar variables
cola = []
inscritos = {}

#función asignación de turno:
#1.Valida que el documento del estudiante este en la lista enviada por el departamento de prácticas

def asig_turno(lista_postu, codigo):    
    if codigo in lista_postu:
        cola.append(codigo)
    
    return cola          
    

#función llama al estudiante respectivo de acuerdo con su posición en la cola y
#registra los siguientes datos en un diccionario:
##Identificación
##Nombre
##Edad
##Inscrito a prácticas (Ingeniería civil, Ingeniería de sistemas, Ingeniería electrónica)
##Fecha y hora del registro

def inscrito_dpa(cola):
    identif = cola.pop(0)
    print('Estudiante con numero de identificación #: ', identif)
    nombre = str(input('Ingrese su nombre: '))
    edad = int(input('Ingrese su edad: '))
    print('Ingrese la facultad donde va a relizar la practica:\n1. Ingenieria Civil\n2. Ingenieria de Sistemas\n3. Ingenieria Electronica')
    facultad = int(input())
    hora_registro = datetime.datetime.now()

    inscritos[identif] = (nombre,edad, facultad, hora_registro)

    return inscritos

#funcion que cuenta y da el % de los inscritos por tipo de programa y genera los siguientes graficos:
#1.Total inscritos a practicas
#2.Total inscritos por tipo de programa
#3.% de inscritos por facultad
  
def inscritos_porprograma(inscritos):
    contar1=0
    contar2=0
    contar3=0
    
    for i in inscritos:
        if inscritos[i][2] == 1:
            contar1 += 1
        if inscritos[i][2] == 2:
            contar2 += 1    
        if inscritos[i][2] == 3:
            contar3 += 1    

    print('El total de inscritos en la facultad de Ingenieria Civil son: ', contar1)
    print('El total de inscritos en la facultad de Ingenieria de Sistemas son: ', contar2)
    print('El total de inscritos en la facultad de Ingenieria Electronica son: ', contar3)

    total = contar1+contar2+contar3

    print('El % de inscritos en la facultad de Ingenieria Civil es: ', round(contar1/total, 2))
    print('El % de inscritos en la facultad de Ingenieria de Sistemas es: ', round(contar2/total, 2))
    print('El % de inscritos en la facultad de Ingenieria Electronica es: ', round(contar3/total, 2)) 

    return ''  
  
    
#Ciclo para asignar un turno al estudiante de manera consecutiva de acuerdo con el orden
#de llegada
#Valida que el estudiante no se haya inscrito ya
n = int(input('Ingrese la cantidad de estudiantes que llegaron: '))
i=0
while i<n:
    cod = int(input('Ingrese el número de identificación del estudiante que se postula: '))
    if cod not in lista_postu:
        print('El estudiante no se encuentra postulado\n')
    elif cod not in inscritos.keys():
        asig_turno(lista_postu, cod)
        inscrito_dpa(cola)       
    else:
        print('Estudiante ya se encuentra inscrito\n')

    i += 1    

print('El total de inscritos a practica son: ', len(inscritos))
print(inscritos_porprograma(inscritos))

#creaciación de la grafica  
#Se crea un grafo vacio
G=nx.Graph()

#Se crean los nodos:
#Nodo DPA
G.add_node("DPA")
#Se crean los nodos de los facultades
G.add_nodes_from(["Ingenieria Sistemas","Ingenieria Civil","Ingenieria Electronica"])
#Se crean los enlaces de las facultades al DPA
G.add_edge("DPA","Ingenieria Sistemas")
G.add_edge("DPA","Ingenieria Civil")
G.add_edge("DPA","Ingenieria Electronica")

#Se dibuja el grafo
nx.draw(G, with_labels=True)
#Se muestra en pantalla
plt.show()
