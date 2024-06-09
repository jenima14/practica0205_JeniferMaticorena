diccionario = {}
print("Ejemplo:     Hola: Hello, Bye: Adiós")
while True:
    usuario = input("Escribe una palabra y su significado en inglés separado por 2 puntos: ")
    if "terminar" in usuario:
        break
    else:
        divisor1 = usuario.split(",")

        for i in divisor1:
            clave, valor = i.split(":")
            diccionario[clave.strip()] = valor.strip()

frase = "hola mi nombre es jenifer"
divisor2 = frase.split(" ")
for j in divisor2:
    traducción = diccionario.get(j,j)
    print(traducción, end=" ")