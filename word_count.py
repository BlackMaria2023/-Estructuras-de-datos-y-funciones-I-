with open("lorem_ipsum.txt", "r") as file:
    lorem_ipsum=file.read()  #read
    print(lorem_ipsum)

#meter todas las letras dentro del set
    
caract = len(set(lorem_ipsum))
palabras = len(set(lorem_ipsum.split(" ")))

print(f"El número de caracteres distintos es: ", caract)
print(f"El número de palabras distintas es: ", palabras)


