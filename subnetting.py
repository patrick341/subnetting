
ipv4=input("Ingrese la direccion ip:  ")
#host=input("Ingrese la cantidad de espacios ocupados para la net:  ")
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
    host=8
elif int(ipv4_vector[0])>127 and int(ipv4_vector[0])<192:
    clase="B"
    print(clase)
    print("su mascara por defecto es 255.255.0.0")
    mascara="255.255.0.0"
    host=16
elif int(ipv4_vector[0])>191 and int(ipv4_vector[0])<224:
    clase="C"
    print(clase)
    print("su mascara por defecto es 255.255.255.0")
    mascara="255.255.255.0"
    host=24   
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
arreglo = [cadena_final_1[i:i+8] for i in range(0, len(cadena_final_1),8)]
print(arreglo)
enteros=[int(i,2) for i in arreglo]
print(enteros)
mascara_adaptada=".".join(str(j) for j in enteros)
print("la mascara de red adaptada es",mascara_adaptada)
print("la nueva notacion de red es: ",host_1)

bits_disponibles=32-host_1

def esposible(bits,hosts):
    if 2**bits-2>= hosts:
        return("es posible")
    else:
        return("es imposible")

host_enteros=int(hosts)
resultado=esposible(bits_disponibles,bits_disponibles)
print(resultado)
host_utilizables=(2**bits_disponibles)-2
print(host_utilizables)

def rango(clase_m):
    if clase_m =="A":
        #print("Esta es una clase A")
        final = mascara_adaptada.split(".")
        afectado = 256-int(final[1])
        rango = afectado    
        print(rango)
        print(subred)
        numero=int(subred)
        print(numero)
        iteracion= 2**bits
        print(iteracion)
        

        for i in range(numero):
            rango_f=rango-1
            #print(rango)
            numero_inicial=numero_decimal2 + i*(rango_f +1)
            numero_final=numero_inicial+rango_f
            lista_ini=[]
            lista_ini.append(numero_decimal1)
            lista_ini.append(numero_inicial)
            lista_ini.append(numero_decimal3)
            lista_ini.append(numero_decimal4)
            lista_fin=[]
            lista_fin.append(numero_decimal1)
            lista_fin.append(numero_final)
            lista_fin.append(numero_decimal3+255)
            lista_fin.append(numero_decimal4+255)
            
            host_ini=numero_inicial + 1
            host_inicial=[]
            host_inicial.append(numero_decimal1)
            host_inicial.append(numero_inicial)
            host_inicial.append(numero_decimal3)
            host_inicial.append(numero_decimal4+1)
            
            
            host_fin=numero_final-1
            host_final=[]
            host_final.append(numero_decimal1)
            host_final.append(numero_final)
            host_final.append(255)
            host_final.append(254)
            #cadena_recurrente_2='.'.join(lista_ini)
            #print("El primer host que debes usar es",numero_inicial,numero_final)
            #print("la lista inicial es: ",lista_ini)
            #print("la lista final es: ",lista_fin)
            cadena_f1 = [str(elemento) for elemento in lista_ini]
            cadena_h1 = [str(elemento) for elemento in host_inicial]
            cadena_recurrente_1='.'.join(cadena_f1)
            cadena_host_1='.'.join(cadena_h1)
            #print("la direccion de subred es",cadena_recurrente_1)
            #print("la primera direccion de host utilizable es: ",cadena_host_1)
            cadena_f2 = [str(elemento) for elemento in lista_fin]
            cadena_h2 = [str(elemento) for elemento in host_final]
            cadena_recurrente_2='.'.join(cadena_f2)
            cadena_host_2='.'.join(cadena_h2)
            #print("la ultima direccion de host utilizable es: ",cadena_host_2)
            #print("la direccion para broadcast es",cadena_recurrente_2)
            print("{:^20} {:^20} {:^20} {:^20}".format("Ip Subred", "Primer Host", "Ultimo Host","Broadcast "))
            print("{:^20} {:^20} {:^20} {:^20}".format(cadena_recurrente_1, cadena_host_1,cadena_host_2, cadena_recurrente_2))

        
    elif clase_m =="B":
        final = mascara_adaptada.split(".")
        afectado = 256-int(final[2])
        rango = afectado    
        print(rango)
        print(subred)
        numero=int(subred)
        print(numero)
        iteracion= 2**bits
        print(iteracion)
        

        for i in range(iteracion):
            rango_f=rango-1
            #print(rango)
            numero_inicial=numero_decimal3 + i*(rango_f +1)
            numero_final=numero_inicial+rango_f
            lista_ini=[]
            lista_ini.append(numero_decimal1)
            lista_ini.append(numero_decimal2)
            lista_ini.append(numero_inicial)
            lista_ini.append(numero_decimal4)
            lista_fin=[]
            lista_fin.append(numero_decimal1)
            lista_fin.append(numero_decimal2)
            lista_fin.append(numero_final)
            lista_fin.append(numero_decimal4+255)
            
            host_ini=numero_inicial + 1
            host_inicial=[]
            host_inicial.append(numero_decimal1)
            host_inicial.append(numero_decimal2)
            host_inicial.append(numero_inicial)
            host_inicial.append(numero_decimal4+1)
            
            
            host_fin=numero_final-1
            host_final=[]
            host_final.append(numero_decimal1)
            host_final.append(numero_decimal2)
            host_final.append(numero_final)
            host_final.append(numero_decimal4+254)
            #cadena_recurrente_2='.'.join(lista_ini)
            #print("El primer host que debes usar es",numero_inicial,numero_final)
            #print("la lista inicial es: ",lista_ini)
            #print("la lista final es: ",lista_fin)
            cadena_f1 = [str(elemento) for elemento in lista_ini]
            cadena_h1 = [str(elemento) for elemento in host_inicial]
            cadena_recurrente_1='.'.join(cadena_f1)
            cadena_host_1='.'.join(cadena_h1)
            #print("la direccion de subred es",cadena_recurrente_1)
            #print("la primera direccion de host utilizable es: ",cadena_host_1)
            cadena_f2 = [str(elemento) for elemento in lista_fin]
            cadena_h2 = [str(elemento) for elemento in host_final]
            cadena_recurrente_2='.'.join(cadena_f2)
            cadena_host_2='.'.join(cadena_h2)
            #print("la ultima direccion de host utilizable es: ",cadena_host_2)
            #print("la direccion para broadcast es",cadena_recurrente_2)
            print("{:^20} {:^20} {:^20} {:^20}".format("Ip Subred", "Primer Host", "Ultimo Host","Broadcast "))
            print("{:^20} {:^20} {:^20} {:^20}".format(cadena_recurrente_1, cadena_host_1,cadena_host_2, cadena_recurrente_2))
    elif clase_m == "C":
        #print("Esta es una clase C")
        final = mascara_adaptada.split(".")
        afectado = 256-int(final[3])
        rango = afectado    
        print(rango)
        print(subred)
        numero=int(subred)
        print(numero)
        iteracion= 2**bits
        print(iteracion)
        

        for i in range(iteracion):
            rango_f=rango-1
            #print(rango)
            numero_inicial=numero_decimal4 + i*(rango_f +1)
            numero_final=numero_inicial+rango_f
            lista_ini=[]
            lista_ini.append(numero_decimal1)
            lista_ini.append(numero_decimal2)
            lista_ini.append(numero_decimal3)
            lista_ini.append(numero_inicial)
            lista_fin=[]
            lista_fin.append(numero_decimal1)
            lista_fin.append(numero_decimal2)
            lista_fin.append(numero_decimal3)
            lista_fin.append(numero_final)
            
            host_ini=numero_inicial + 1
            host_inicial=[]
            host_inicial.append(numero_decimal1)
            host_inicial.append(numero_decimal2)
            host_inicial.append(numero_decimal3)
            host_inicial.append(numero_inicial+1)
            
            
            host_fin=numero_final-1
            host_final=[]
            host_final.append(numero_decimal1)
            host_final.append(numero_decimal2)
            host_final.append(numero_decimal3)
            host_final.append(numero_final-1)
            #cadena_recurrente_2='.'.join(lista_ini)
            #print("El primer host que debes usar es",numero_inicial,numero_final)
            #print("la lista inicial es: ",lista_ini)
            #print("la lista final es: ",lista_fin)
            cadena_f1 = [str(elemento) for elemento in lista_ini]
            cadena_h1 = [str(elemento) for elemento in host_inicial]
            cadena_recurrente_1='.'.join(cadena_f1)
            cadena_host_1='.'.join(cadena_h1)
            #print("la direccion de subred es",cadena_recurrente_1)
            #print("la primera direccion de host utilizable es: ",cadena_host_1)
            cadena_f2 = [str(elemento) for elemento in lista_fin]
            cadena_h2 = [str(elemento) for elemento in host_final]
            cadena_recurrente_2='.'.join(cadena_f2)
            cadena_host_2='.'.join(cadena_h2)
            #print("la ultima direccion de host utilizable es: ",cadena_host_2)
            #print("la direccion para broadcast es",cadena_recurrente_2)
            print("{:^20} {:^20} {:^20} {:^20}".format("Ip Subred", "Primer Host", "Ultimo Host","Broadcast "))
            print("{:^20} {:^20} {:^20} {:^20}".format(cadena_recurrente_1, cadena_host_1,cadena_host_2, cadena_recurrente_2))

rango(clase)

