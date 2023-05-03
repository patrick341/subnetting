
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

numero_decimal1 = int(ipv4_vector[0])
numero_decimal2 = int(ipv4_vector[1])
numero_decimal3 = int(ipv4_vector[2])
numero_decimal4 = int(ipv4_vector[3])

#modulos = [] 

def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario





print(str(decimal_a_binario(numero_decimal1)).zfill(8))
print(str(decimal_a_binario(numero_decimal2)).zfill(8))
print(str(decimal_a_binario(numero_decimal3)).zfill(8))
print(str(decimal_a_binario(numero_decimal4)).zfill(8))
for i in range(4):
    list1.append(str(decimal_a_binario(int(ipv4_vector[i]))).zfill(8))

print(list1)


def saber_n(a):
    flag=True
    c=0
    while ( flag == True):
        if 2**c >= int(a):
            flag = False
        else:
            c=c+1
            flag = True
    return c 

mascara_vector=mascara.split('.')
bits = saber_n(subred)
print(saber_n(subred))        
print(str(decimal_a_binario(int(mascara_vector[0]))).zfill(8))
print(str(decimal_a_binario(int(mascara_vector[1]))).zfill(8))
print(str(decimal_a_binario(int(mascara_vector[2]))).zfill(8))
print(str(decimal_a_binario(int(mascara_vector[3]))).zfill(8))
lista3=[]
host_1=int(host)
print(host_1)
host_1 = host_1 +bits
print(host_1)
cadena=""
for i in range(host_1): 
    cadena = cadena + "1"
print(len(cadena))
cadena_final=cadena.zfill(32)
print(cadena.zfill(32))
cadena_final_1= cadena_final[::-1]
print(cadena_final_1)


#cadena.zfill(32)    
#for i in range(4):
#    if str(decimal_a_binario(int(mascara_vector[i]))) != "00000000":
#        lista3.append(str(decimal_a_binario(int(mascara_vector[i]))))

#print(lista3)    


def cambio_mascara():
    print(mascara)
    decimal_a_binario(int(mascara[0]))
    decimal_a_binario(int(mascara[1]))
    decimal_a_binario(int(mascara[2]))
    decimal_a_binario(int(mascara[3]))



#numero_bin= ''.join(modulos)
#print(numero_bin)