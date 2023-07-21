import re

regex = r"\b\w{4}\b"
regex2 = r"-"
texto = "Este texto contiene la palabra pala"
texto2 = "Manzana-Pera-Uva-Sandía"
reemplazo = "TEST"

# devuelve la primera coincidencia
# resultado = re.search(regex, texto)

# devuelve todas las coincidencias
# resultado = re.findall(regex, texto)

# sustituye reemplazo en donde coincide regex en texto
# resultado = re.sub(regex, reemplazo, texto)

# divide el texto según regex
# resultado = re.split(regex2, texto2)

resultado = re.findall(r"abc[0-9]+", "abc00123yz456_0")

if resultado:
    print(resultado)
else:
    print("No hay coincidencias")
