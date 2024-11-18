## lambdas ## 

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 8))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(3, 3))

def sum_three_values(value):
  return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2,4))


