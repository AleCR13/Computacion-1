#Una profesora de ciencias humanas de la facultad de ingenieria quiere llevar a sus estudiantes a una excursion a una empresa para que conozcan la labor de campo de los ingenieros
#como algunos son menores de edad necesitara el permiso de sus padres para llevarlos, entonces le pide el favor
#a un estudiante que esta cursando la materia de compu1 que le escriba un codigo que cree un archivo de texto con los estudiantes mayores de edad y otro con los menores de edad
#para asi ella saber a quien le debe dar una planilla de permiso 

arch1 = open('registro.txt', 'r')
# Archivos a generar
arch2 = open('Mayores.txt', 'w')
arch3 = open('Menores.txt', 'w')

# Recorrido del archivo
for registro in arch1:
    # Devuelve una lista con los campos del registro
    linea = registro.split(',')
    print(linea)

    #Procesar elementos:
    #Utilizar archivo para leer la lista
    nombre = linea[0]     # Nombre del estudiante
    print(nombre)
    cedula = linea[1]     # Cédula del estudiante
    print(cedula)
    edad = int(linea[2])  # edad del estudiante
    print(edad)
    if edad >= 18:  # va al paseo
        arch2.write(nombre +', ' + cedula + '\n')
    else:  # mayor de edad
        arch3.write(nombre + ', '+ cedula + '\n')

# Cerrar archivos
arch1.close()
arch2.close()
arch3.close()

# Escritura de resultados
print('la informacion se encuentra en los archivos mayores.txt y menores.txt que encontrara en el escritorio ')