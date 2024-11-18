from functools import reduce

## Higher Functions ## 


def sum_one(value):
  return value + 1
  
def sum_five(value):
  return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum): # Esto es una funcion de order superior, esta funcion mediante la variable f_sum despues llama a otra funcion creada afuera
  return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one)) # Saldria 8
print(sum_two_values_and_add_value(5, 2, sum_five)) # Saldria 12

## Closures ## 

def sum_ten(original_value): # Closure funcion que define una funcion y retorna una funcion
  def add(value):
    return value + 10 + original_value
  return add

add_closure = sum_ten(1)
print(add_closure(5))



## built-in higher order functions ##

numbers = [2, 5, 10, 21]

# Map

def multiply_two(number):
  return number * 2
 
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers))) # Aca tiene todo el sentido del mundo usar una lambda, para no estar definiendo afuera esa funcion tan especifica

# Filter 

def filter_greater_that_ten(number):
  if number > 10:
    return True
  return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))  # Aca tiene todo el sentido del mundo usar una lambda, para no estar definiendo afuera esa funcion tan especifica


# Reduce 

def sum_two_values(first_value, second_value): # Esto va por ejemplo sumando 2 + 5 primeros valores y despues pasa al siguiente y asi sucesivamente, los junta, y los suma
  return first_value + second_value

print(reduce(sum_two_values, numbers))




