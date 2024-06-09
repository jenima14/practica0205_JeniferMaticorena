diccionario_alumnos = {}
while True:
    opción = int(input('''\n(1) Añadir alumno/a
(2) Eliminar alumno/a
(3) Mostrar alumno/a
(4) Listar todo el alumnado
(5) Listar alumnado aprobado
(6) Terminar: '''))
    print()
    if opción == 6:
        break
    elif opción == 1:
        diccionario_datos = {}
        datos = ["nombre","apellido","teléfono","correo electronico","aprobado"]
        NIF = input("Escribe tu NIF: ")
        for i in datos:
            diccionario_datos[i] = input(f"Escribe tu {i}: ")
        diccionario_alumnos[NIF] = diccionario_datos
 
    elif opción == 2:
        alumno = input("Escribe tu NIF: ")
        if alumno in diccionario_alumnos:
            del diccionario_alumnos[alumno]
            print(f"NIF: {alumno} fue elimindo")
        else:
            print(f"El NIF: {alumno} no se encuentra registrado")

    elif opción == 3:
        alumno = input("Escribe tu NIF: ")
        if alumno in diccionario_alumnos.keys():
                for clave, valor in diccionario_alumnos[alumno].items():
                    print(clave + " : " + valor)
        else:
            print(f"El NIF {alumno} no se encuentra registrado\n")
    
    elif opción == 4:
        nif = diccionario_alumnos.keys()
        nombres = diccionario_datos.values()
        for x,y in zip(nif,nombres):
            print(f"NIF: {x} Nombre: {y}")
    
    elif opción == 5:
        nif = diccionario_alumnos.keys()
        nombres = diccionario_datos.values()
        aprobado = diccionario_datos["aprobado"] >= "5"
        for a,b in zip(nif, nombres):
            if aprobado:
                print(f"NIF: {a} Nombre: {b}")