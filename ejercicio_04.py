lista = ["nombre","edad","sexo","teléfono","correo electrónico"]
diccionario = {}

for i in lista:
    usuario = input(f"Ingresa tu {i}: ")
    diccionario[i] = usuario
    print(diccionario)