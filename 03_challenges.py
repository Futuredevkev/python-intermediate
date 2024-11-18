## Challenges ## 

"""
  EL FAMOSO FIZZBUZZ
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  Múltiplos de 3 por la palabra "fizz".
  Múltiplos de 5 por la palabra "buzz".
  Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

numbers_one_to_one_hundred = [i for i in range (1, 101)] # Creamos una lista con los números del 1 al 100

def fizzbuzz():
  for number in numbers_one_to_one_hundred: # Recorremos la lista y lo imprimimos
    if number % 3 == 0 and number % 5 == 0: 
      print(f'el numero {number}, es divisible por 3 y por 5, por lo tanto es fizz')
    elif number % 3 == 0:
      print(f'el numero {number}, es divisible por 3, por lo tanto es buzz')
    elif number % 5 == 0: 
      print(f'el numero {number}, es divisible por 5, por lo tanto es fizzbuzz')
    else:
      print(f'el numero {number}, no es divisible por 3 o por 5') 
  
  
fizzbuzz()


"""
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
  NO hace falta comprobar que ambas palabras existan.
  Dos palabras exactamente iguales no son anagrama.
 """
 
 
def anagram(word1, word2):
  if word1.lower() == word2.lower():
    return False
  return sorted(word1.lower()) == sorted(word2.lower()) # Usamos sorted para ordenar cada palabra en una lista y comprobar si son iguales, sort en cambio sirve mas para cuando tenes una lista y la queres ordenar



print(anagram('Amor', 'Roma'))


"""
  Escribe un programa que imprima los 50 primeros números de la sucesión
  de Fibonacci empezando en 0.
  La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""



def fibonacci():
  prev= 0
  next= 1
  
  for index in range(0, 51):
    print(prev)
    
    fib = prev + next 
    prev = next 
    next = fib
    
fibonacci()


"""
  Escribe un programa que se encargue de comprobar si un número es o no primo.
  Hecho esto, imprime los números primos entre 1 y 100.
"""



def is_prime():
    for number in range(0, 101):
      if number >= 2:
        is_divisble = False
  
        for index in range(2, number):
          if number % index == 0:
            is_divisble = True 
            break
    
        if not is_divisble:
          print(number)
          
is_prime()


 
"""
  crea un programa que invierta el orden de una cadena de texto
  sin usar funciones propías del lenguaje que lo hagan de forma automatica.
"""
 
 
def reverse(text):
  text_len = len(text)
  reversed_text = ""
  for index in range(0, text_len):
    reversed_text += text[text_len - index - 1] 
  return reversed_text
  

print(reverse("clash royale"))




"""
 Crea una única función (importante que sólo sea una) que sea capaz
 de calcular y retornar el área de un polígono.
  La función recibirá por parámetro sólo UN polígono a la vez.
  Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  Imprime el cálculo del área de un polígono de cada tipo.
"""


"""
def poligono(figure, b=None, h= None, l=None):
  if figure == 'triangulo':
    area = b * h / 2
    return f'la area del triangulo es {area}'
  elif figure == 'cuadrado':
    area = l ** 2
    return f'el area del cuadrado es {area}'
  elif figure == 'rectangulo':
    area = b * h
    return f'el area del rectangulo es {area}'
  else: 
    print('Ninguno coincide con las figuras permitidas en la aplicacion')
    
  
def calcular_area_interactiva():
    print("¡Bienvenido al calculador de áreas de polígonos!")
    print("Figuras soportadas: triangulo, cuadrado, rectangulo")
    
 
    figure = input("¿Qué figura quieres calcular? ").lower()

  
    if figure == 'triangulo':
        print("Necesitas ingresar la base y la altura del triángulo.")
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        resultado = poligono(figure, b=base, h=altura)

    elif figure == 'cuadrado':
        print("Necesitas ingresar el lado del cuadrado.")
        lado = float(input("Ingresa el lado: "))
        resultado = poligono(figure, l=lado)

    elif figure == 'rectangulo':
        print("Necesitas ingresar la base y la altura del rectángulo.")
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        resultado = poligono(figure, b=base, h=altura)

    else:
        resultado = "Figura no reconocida. Por favor, selecciona triangulo, cuadrado o rectangulo."

  
    print(resultado)


calcular_area_interactiva()
"""





""" 
cuantas veces se repita una palabra en una lista, sin usar metodos del sistema 
"""


def countRepeat(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)): 
            if words[i] == words[j]:  
                count += 1
                break  
    return count

words = ['leche', 'pancho', 'leche', 'conaprole', 'vascolet', 'pancho']
repeated_count = countRepeat(words)
print(f"Palabras repetidas en la lista: {repeated_count}")