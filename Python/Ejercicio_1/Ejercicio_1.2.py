Frase = input("Hola como estas dame una frase y te calculo cuanto tardarias en decirla: ")
palabras_separadas = Frase.split(" ")
cantidad_palabras = len(palabras_separadas)
print(f"Amigo dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} en dedecirla")
print(f"Dalto lo diria en {cantidad_palabras * 100 /2 * 1.3 / 100} segundos en decirlo")

if cantidad_palabras > 30:
    print ("Te pasas era una frase no una historia de tu vida")

