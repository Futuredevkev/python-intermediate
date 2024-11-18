import re

# match
# Busca una coincidencia al comienzo de la cadena.

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# Coincide si el inicio del string corresponde con el patrón.
match = re.match("Esta es la lección", my_string, re.I)  # re.I hace la búsqueda insensible a mayúsculas y minúsculas.
print(match)  # Devuelve un objeto Match si hay coincidencia, de lo contrario, None.
start, end = match.span()  # Obtiene las posiciones de inicio y fin de la coincidencia.
print(my_string[start:end])  # Muestra la porción del string que coincide con el patrón.

# Otro ejemplo con un string diferente.
match = re.match("Esta no es la lección", my_other_string)
if match is not None:  # Verifica si hay una coincidencia.
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# Aquí no hay coincidencia porque "Expresiones Regulares" no está al principio de la cadena.
print(re.match("Expresiones Regulares", my_string))

# search
# Busca la primera aparición del patrón en cualquier parte del string.

search = re.search("lección", my_string, re.I)  # Insensible a mayúsculas y minúsculas.
print(search)  # Devuelve un objeto Match si encuentra el patrón.
start, end = search.span()  # Obtiene las posiciones de inicio y fin.
print(my_string[start:end])  # Muestra la coincidencia encontrada.

# findall
# Devuelve todas las coincidencias como una lista.

findall = re.findall("lección", my_string, re.I)  # Insensible a mayúsculas y minúsculas.
print(findall)  # Lista con todas las apariciones del patrón.

# split
# Divide el string en una lista utilizando el patrón como delimitador.

print(re.split(":", my_string))  # Divide la cadena donde encuentra ":".

# sub
# Reemplaza todas las apariciones del patrón con una cadena nueva.

print(re.sub("[l|L]ección", "LECCIÓN", my_string))  # Reemplaza "lección" o "Lección" por "LECCIÓN".
print(re.sub("Expresiones Regulares", "RegEx", my_string))  # Reemplaza "Expresiones Regulares" por "RegEx".

# Patrones de expresiones regulares

# Coincide con "lección" o "Lección".
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

# Coincide con "lección", "Lección" o "Expresiones".
pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

# Busca cualquier dígito (0-9).
pattern = r"[0-9]"
print(re.findall(pattern, my_string))  # Encuentra todos los números.
print(re.search(pattern, my_string))  # Encuentra la primera aparición de un número.

# Equivalente a buscar cualquier dígito (\d es un atajo).
pattern = r"\d"
print(re.findall(pattern, my_string))

# Busca cualquier carácter que no sea un dígito.
pattern = r"\D"
print(re.findall(pattern, my_string))

# Busca palabras que comiencen con "l" seguidas de cualquier cosa (.* significa "cualquier cosa").
pattern = r"[l].*"
print(re.findall(pattern, my_string))

# Validación de correo electrónico

email = "mouredev@mouredev.com"
# Patrón para validar correos electrónicos.
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))  # Verifica si el correo coincide con el patrón desde el principio.
print(re.search(pattern, email))  # Busca si el correo contiene el patrón.
print(re.findall(pattern, email))  # Devuelve una lista con el correo si coincide.

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))  # También valida correos con dominios más largos.
