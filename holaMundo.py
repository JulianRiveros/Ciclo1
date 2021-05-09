print("Hello world")
var=1

print(type(var)) ##Devuelve el tipo de variable
var=var**2 #El doble ** indica potencia
var2="hola"
print(len(var2)) #Indica el numero de caracteres de la variable
'''
var3=int(input("Ingrese el valor de la variable: "))
if var3>40:
    print("Mayor a 40")
elif  var3>30 and var3<=40:
    print("entre 31 y 40") 
else:    
    print("menor o igual a 30")   
'''

peso=float(input("Digite el peso de la persona: "))
Altura=float(input("Digite la altura de la persona: "))

IMC=peso/(Altura**2)

if IMC< 17.5:
    print("Peso insuficiente")
elif  IMC>=17.5 and IMC<25.9:
    print("Peso estándar")
elif IMC>=26 and IMC<31:
    print("Sobrepeso")
else:
    print("Obesidad")  
  
print("Version 2 commit")
print("Probando ramas")