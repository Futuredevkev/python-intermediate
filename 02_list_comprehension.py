## List Comprehension ##

my_original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_original_list)


my_list = [i for i in range(0, 81)] # itera cada uno de los elemenots y Crea una lista con los números del 0 al 80
print(my_list)

# Tambien podemos realizar operaciones en este bucle 

my_list = [i * 2 for i in range(0, 81)] # itera en cada elemento y multiplica por 2
print(my_list)

my_list = [i + 2 for i in range(0, 81)] # itera en cada elemento y suma 2
print(my_list)

my_list = [i * i for i in range(0, 81)] # itera en cada elemento y se multiplica por si mismo
print(my_list)

# Funcion que suma 5 a un numero
def sum_five(number):
  return number + 5

my_list = [sum_five(i) for i in range(0, 15)]  # itera en cada elemento y le suma 5 mediante una función
print(my_list)