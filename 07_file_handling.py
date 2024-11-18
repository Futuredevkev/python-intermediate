import os

## File Handling ##


# .txt file 

txt_file = open("./my_file.txt", 'r+')
print(txt_file.read())
print(txt_file.read(10)) # Lee los primeros diez caracteres 
print(txt_file.readline()) # Lee por linea 
print(txt_file.readlines()) # Hace un listado del texto por lineas


for line in txt_file.readlines(): # Por ejemplo aca va a leer todas lineas haciendola un listado, haciendo un for y sacando c/1 por consola
  print(line)
  

txt_file.write("\nSoy gay") # Me va a escribir esto en el documento

txt_file.close() # Buena practica para cerrar el fichero al terminar de hacer cosas 

# os.remove("./my_file.txt") # Eliminar fichero




#.json file 

import json

json_file = open("./my_file.json", 'w+')

json_test = {
  "Nombre": "Kevin",
  "Apellido": "Moreira",
  "Edad": 22, 
  "Language": "Python"
}

json.dump(json_test, json_file, indent=4) # Crear JSON con indentado

json_file.close()
  
json_dict = json.load(open("./my_file.json")) # Leerlo y transformarlo en un dict
print(json_dict)


#.csv file

import csv 

csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Kevin", "Moreira", "22", "Python"])

#.xlsx file 
#import xlrd #debe instalarse el modulo 

#.xml file 

import xml 