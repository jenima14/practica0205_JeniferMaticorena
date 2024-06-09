diccionario = {"Pan":1.40, "Huevos":2.30, "Cebolla":0.85, "Aceite":4.35}

articulo = input("Escriba el nombre de un producto: ").capitalize()
unidades = int(input("Escriba un número de unidades: "))

if articulo in diccionario.keys():
    print(f"Producto: {articulo} Precio: {diccionario[articulo]}")
    print(f"Tus unidades: {unidades}     Total: {unidades * diccionario[articulo]}")
else:
    print(f"El artículo {articulo} no está en el diccionario")