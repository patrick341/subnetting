
ipv4=input("Ingrese la direccion ip:  ")
host=input("Ingrese la cantidad de espacios ocupados para la net:  ")
subred=input("Ingrese la cantidada de subredes:  ")
hosts=input("Cantidad maxima de host:  ")
list1=[]
ipv4_vector=ipv4.split('.')
print(ipv4_vector)  
if int(ipv4_vector[0])>0 and int(ipv4_vector[0])<128 :
    clase="A"
    print(clase)
    print("su mascara por defecto es 255.0.0.0")
    mascara="255.0.0.0"
elif int(ipv4_vector[0])>127 and int(ipv4_vector[0])<192:
    clase="B"
    print(clase)
    print("su mascara por defecto es 255.255.0.0")
    mascara="255.255.0.0"
elif int(ipv4_vector[0])>191 and int(ipv4_vector[0])<224:
    clase="C"
    print(clase)
    print("su mascara por defecto es 255.255.255.0")
    mascara="255.255.255.0"
       
for i in ipv4:
    i=ipv4.split('.')

print(clase)
print(mascara)

print(ipv4)
print(list1)