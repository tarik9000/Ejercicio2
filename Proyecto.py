"""
Trabajas para una empresa donde los vendedores reciben comisiones del 18% por sus ventas totales, 
y tu jefe quiere que ayudes a los vendedores a calcular sus comisiones. ¿Cómo? Vas a crear un programa que les pregunte nombre y cuánto han vendido este mes. 
Tu programa le va a responder con una frase que incluya su nombre y la cantidad que le corresponde por las comisiones.

Esto no es un programa complejo, pero es entendible que pueda complicarse cuando estás aprendiendo. Por más que lo que has aprendido hasta ahora es muy simple, 
ponerlo todo junto en un solo programa puede ser complejo, por lo que te doy un par de consejos:

- Deberías comenzar preguntando cosas al usuario, así que necesitarás input para poder recibir los datos del teclado. Deberías usar las variables para almacenar los ingresos. 
Recuerda que esos ingresos se almacenan como strings, así que deberás convertir uno de esos ingresos en float para poder hacer operaciones.
- Recuerda almacenar los datos en variables
- Sería ideal que para imprimir en pantalla el resultado te asegures de que esa información no tenga más de dos decimales para que sea fácil de leer. 
Organiza todo en un string al que debes dar formato. Recuerda que hay dos formas posibles de hacer dicho formato.
"""
nombre=input("¿Cual es tu nombre? ")
ventas=float(input("¿Cuanto has vendido? "))
print("Hola "+nombre+" has vendido "+str(ventas)+" en total te corresponde "+str(round(ventas*18/100),2))