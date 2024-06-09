diccionario = {}
datos = ["Nombre","Edad","Dirección","Teléfono"]
datos_usuario = []
for i in datos:
    usuario = input(f"Escribe tu {i}: ")
    datos_usuario.append(usuario)
   
for j in range(len(datos_usuario)):
    diccionario[datos[j]] = datos_usuario[j]
 
print(f"{diccionario['Nombre']} tiene {diccionario['Edad']} años, vive en {diccionario['Dirección']} y su número de teléfono es {diccionario['Teléfono']}.")