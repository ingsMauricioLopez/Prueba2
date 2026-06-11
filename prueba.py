print("Inicio de proyecto")
# Definición de variables
#nombre = input("Ingrese su nombre: ")
#edad = int(input("Ingrese su edad: "))

#print("Hola", nombre)
#print("Tu edad es:", edad)

# Condición
#if edad >= 18:
#    print("Eres mayor de edad")
#else:
#    print("Eres menor de edad")

num=[7,2,3,10,1,6,5,8,4,9]
print(num)

"Ordenamiento burbuja"
cambio=True
n=0
while ( cambio):
    n+=1
    cambio=False
    for i in range (len(num)-1):    
        if(num[i]>num[i+1]):
            cambio=True
            num[i],num[i+1]=num[i+1],num[i]        
        print(num)
    print(n)
