"""
1. Declara dos variables, llamadas nombre y edad. Usa tu nombre y 
tu edad para asignarles valor a las variables
"""
nombre = "tarek"
edad = 25
"""
2. Crea tres variables:
   a) nombre
   b) apellido
   c) nombre_completo
   Usa tu nombre y tu apellido, y luego en nombre_completo realiza la concatenación
"""
nombre = "tarek"
apellido = "benyasine"
nombre_completo = nombre +" "+ apellido
"""
3. Declara la variable libro, y asígnale el valor “Python”, 
y muéstralo por pantalla con la frase: “Estoy aprendiendo Python gracias a este libro de libro”. 
Para ello, debes concatenar la primera parte de la frase con el valor que tendrá la variable. 
Recuerda generar un espacio antes de concatenar la variable al resto del texto.

"""
libro="Python"
print("Estoy aprendiendo Python gracias a este libro de "+libro)
"""
4. Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección. Imprime el tipo de dato de dicha variable.
"""
num_entero=1
print(type(num_entero))
"""
5. Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección
"""
num_decimal=2.2
"""
6. ¿De qué tipo es el resultado de la suma de 7,5 + 2,5? Genera el código para verificarlo. Para ello, crea dos variables:
   a) num1 = 7.5
   b) num2 = 2.5
   A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

"""
num1 = 7.5
num2 = 2.5
resultado = num1+num2
print(type(resultado))
"""
7. Convierte el valor de num1 en un int e imprime el tipo de dato que resulta
"""

num1 = int(num1)
print(type(num1))
"""
8. Convierte el valor de num2 en un float e imprime el tipo de dato que resulta
"""
num2=2
num2= float(num2)
print(type(num2))
"""
9. Suma los valores de num1 y num2. No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
"""
print(num1+int(num2))
"""
10. Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase: “Estimado/a (nombre_asociado), 
su número de asociado es: (numero_asociado)” Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
nombre_asociado="Pepe"
numero_asociado= 923512
print("Estimado/a "+nombre_asociado+", su número de asociado es: "+str(numero_asociado))
"""
11. Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase: “Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos” 
Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
puntos_nuevos=5
puntos_totales=15
puntos_totales=puntos_nuevos+puntos_totales
print("Has ganado "+str(puntos_nuevos)+" puntos! En total, acumulas "+str(puntos_totales)+" puntos")
"""
12. Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase: “Has ganado (puntos_nuevos) puntos! En total, 
acumulas (puntos_totales) puntos” En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos. 
Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
puntos_nuevos=5
puntos_anteriores=15
puntos_totales=puntos_nuevos+puntos_anteriores
print("Has ganado "+str(puntos_nuevos)+" puntos! En total, acumulas "+str(puntos_totales)+" puntos")
"""
13. Muestra en pantalla el cociente (división) de los siguientes dos números: 874 dividido entre 27. Debes mostrar solo el valor numérico que resulta de esta operación.
"""
print(874/27)
"""
14. Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33. Debes mostrar solo el valor numérico que resulta de esta operación
"""
print(456%33)
"""
15. Calcula y muestra en pantalla la raíz cuadrada de 783. Debes mostrar solo el valor numérico que resulta de esta operación.
"""
print(783**0.5)
"""
16. Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
"""
print(round(10/3,2))
"""
17. Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
"""
print(round(10.676767))
"""
18. Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
"""
print(round(5**0.5,4))