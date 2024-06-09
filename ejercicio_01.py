diccionario =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
usuario = input("Escriba el nombre de una divisa: ").capitalize()

if usuario in diccionario.keys():
    print(f"Símbolo de tu divisa {diccionario[usuario]}")
else:
    print(f"La divisa '{usuario}' no está en el diccionario")