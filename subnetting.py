'''
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
    host=16   
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

'''

'''
# Calculo del rango de subredes
direccion_ip_bin = "".join(list1)
direccion_red_bin = direccion_ip_bin[0:host_1] + "0" * bits_disponibles
direccion_broadcast_bin = direccion_ip_bin[0:host_1] + "1" * bits_disponibles
direccion_red = ".".join([str(int(direccion_red_bin[i:i+8],2)) for i in range(0,32,8)])
direccion_broadcast = ".".join([str(int(direccion_broadcast_bin[i:i+8],2)) for i in range(0,32,8)])

print("La dirección de red es: ", direccion_red)
print("La dirección de broadcast es: ", direccion_broadcast)

direccion_primera_subred_bin = direccion_red_bin[:host_1] + "0" * bits_disponibles + "1"
direccion_ultima_subred_bin = direccion_broadcast_bin[:host_1] + bin(int("1" * bits_disponibles, 2) - 1)[2:].zfill(bits_disponibles)
#direccion_ultima_subred_bin = direccion_broadcast_bin[:host_1] + "1" * bits_disponibles - 1
direccion_primera_subred = ".".join([str(int(direccion_primera_subred_bin[i:i+8],2)) for i in range(0,32,8)])
direccion_ultima_subred = ".".join([str(int(direccion_ultima_subred_bin[i:i+8],2)) for i in range(0,32,8)])

print("La dirección de la primera subred es: ", direccion_primera_subred)
print("La dirección de la última subred es: ", direccion_ultima_subred)

rango_subredes = []
for i in range(int(subred)):
    direccion_subred_bin = direccion_red_bin[:host_1] + bin(i)[2:].zfill(bits_disponibles)
    direccion_subred = ".".join([str(int(direccion_subred_bin[i:i+8],2)) for i in range(0,32,8)])
    direccion_broadcast_subred_bin = direccion_subred_bin[:host_1] + "1" * bits_disponibles
    direccion_broadcast_subred = ".".join([str(int(direccion_broadcast_subred_bin[i:i+8],2)) for i in range(0,32,8)])
    direccion_primera_direccion_host_subred_bin = direccion_subred_bin[:host_1] + "0" * bits_disponibles + "1"
    direccion_primera_direccion_host_subred = ".".join([str(int(direccion_primera_direccion_host_subred_bin[i:i+8],2)) for i in range(0,32,8)])
    direccion_ultima_direccion_host_subred_bin = direccion_broadcast_subred_bin[:host_1] + "0" * bits_disponibles + "1"
    direccion_ultima_direccion_host_subred = ".".join([str(int(direccion_ultima_direccion_host_subred_bin[i:i+8],2)) for i in range(0,32,8)])
    rango_subred = [direccion_subred, direccion_broadcast_subred, direccion_primera_direccion_host_subred, direccion_ultima_direccion_host_subred]
    rango_subredes.append(rango_subred)

print("\n\n")
print("|Dirección de subred  |Dirección Broadcast  |Primera Dirección Host  |Última Dirección Host|")
print("|--------------------|---------------------|------------------------|----------------------|")
for i in rango_subredes:
    print("|{:20}|{:21}|{:24}|{:22}|".format(i[0], i[1], i[2], i[3]))

'''




#binarios = ["10101010", "11110000", "00110011", "01010101"]
#enteros = [int(binario, 2) for binario in binarios]
#print(enteros)


#entero_array = [int(subcadena,16) for subcadena in arreglo]
#print(entero_array)
#cadena = "0123456789abcdef0123456789abcdef"
#arreglo = [cadena[i:i+8] for i in range(0, len(cadena), 8)]
#print(arreglo)
#cadena.zfill(32)    
#for i in range(4):
#    if str(decimal_a_binario(int(mascara_vector[i]))) != "00000000":
#        lista3.append(str(decimal_a_binario(int(mascara_vector[i]))))

#print(lista3)    

'''
def cambio_mascara():
    print(mascara)
    decimal_a_binario(int(mascara[0]))
    decimal_a_binario(int(mascara[1]))
    decimal_a_binario(int(mascara[2]))
    decimal_a_binario(int(mascara[3]))
'''


#numero_bin= ''.join(modulos)
#print(numero_bin)



# Obtener las direcciones de red y broadcast para cada subred
'''
direccion_ip = [int(octeto) for octeto in ipv4_vector]
direccion_binaria = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*direccion_ip)
direccion_red_bin = direccion_binaria[:32-bits_disponibles] + '0'*bits_disponibles
direccion_broadcast_bin = direccion_red_bin[:32-bits] + '1'*bits
direccion_ultima_subred_bin = direccion_broadcast_bin[:32-bits_disponibles] + '1'*bits_disponibles
direccion_ultima_subred_dec = [int(direccion_ultima_subred_bin[i:i+8], 2) for i in range(0, 32, 8)]

# Mostrar información de cada subred
print(f"\nInformación de subredes para la dirección IP {ipv4} con máscara de subred {mascara_adaptada}:\n")
print("Subred\t\tDirección de red\t\t\tDirección de broadcast\t\tÚltima dirección de subred")
for i in range(int(subred)):
    direccion_red_dec = [int(direccion_red_bin[j:j+8], 2) for j in range(0, 32, 8)]
    direccion_broadcast_dec = [int(direccion_broadcast_bin[j:j+8], 2) for j in range(0, 32, 8)]
    direccion_ultima_subred_dec = [int(direccion_ultima_subred_bin[j:j+8], 2) for j in range(0, 32, 8)]
    print(f"{i+1}\t\t{direccion_red_dec[0]}.{direccion_red_dec[1]}.{direccion_red_dec[2]}.{direccion_red_dec[3]}\t\t"
          f"{direccion_broadcast_dec[0]}.{direccion_broadcast_dec[1]}.{direccion_broadcast_dec[2]}.{direccion_broadcast_dec[3]}\t\t\t"
          f"{direccion_ultima_subred_dec[0]}.{direccion_ultima_subred_dec[1]}.{direccion_ultima_subred_dec[2]}.{direccion_ultima_subred_dec[3]}")
    direccion_ip_decimal = int(ipv4.replace('.', ''))
    direccion_ip_decimal = direccion_ip_decimal + 2**(bits_disponibles)
    direccion_ip_binaria = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*direccion_ip_decimal)
    direccion_red_bin = direccion_ip_binaria[:32-bits_disponibles] + '0'*bits_disponibles
    direccion_broadcast_bin = direccion_red_bin[:32-bits] + '1'*bits
    direccion_ultima_subred_bin = direccion_broadcast_bin[:32-bits_disponibles] + '1'*bits_disponibles

'''

import re

def obtener_mascara_red(num_bits_subredes=None, num_bits_hosts=None):
    """
    Calcula la máscara de red para una cantidad de bits especificada para subredes y/o hosts.
    """
    num_bits = 0
    if num_bits_subredes is not None:
        num_bits += num_bits_subredes
    if num_bits_hosts is not None:
        num_bits += num_bits_hosts
    mascara_red_bin = "1" * num_bits + "0" * (32 - num_bits)
    mascara_red_octetos = [int(mascara_red_bin[i:i+8], 2) for i in range(0, 32, 8)]
    mascara_red = ".".join(str(octeto) for octeto in mascara_red_octetos)
    return mascara_red


def obtener_direccion_red(direccion_ip, mascara_red):
    """
    Calcula la dirección de red para una dirección IP y una máscara de red dadas.
    """
    octetos_ip = direccion_ip.split(".")
    octetos_mascara = mascara_red.split(".")
    direccion_red = [int(octetos_ip[i]) & int(octetos_mascara[i]) for i in range(4)]
    direccion_red = ".".join(str(octeto) for octeto in direccion_red)
    return direccion_red



def verificar_direccion_ip(direccion_ip, num_bits_subredes=None, num_bits_hosts=None):
    """
    Verifica si una dirección IP es válida. Si se especifica la cantidad de bits para subredes y/o hosts,
    también verifica si la dirección de red y la máscara de red tienen suficientes bits para la cantidad
    de subredes y/o hosts especificados.
    """
    octetos = direccion_ip.split(".")
    if len(octetos) != 4:
        return False
    for octeto in octetos:
        try:
            octeto_int = int(octeto)
        except ValueError:
            return False
        if octeto_int < 0 or octeto_int > 255:
            return False
    if num_bits_subredes is not None and num_bits_hosts is not None:
        mascara_red = obtener_mascara_red(num_bits_subredes=num_bits_subredes, num_bits_hosts=num_bits_hosts)
        direccion_red = obtener_direccion_red(direccion_ip, mascara_red)
        if not verificar_direccion_ip(mascara_red) or not verificar_direccion_ip(direccion_red):
            return False
        num_bits_total = num_bits_subredes + num_bits_hosts
        num_bits_mascara_red = sum([bin(int(octeto))[2:].count("1") for octeto in mascara_red.split(".")])
        if num_bits_total > 32 or num_bits_total > (32 - num_bits_mascara_red):
            return False
    return True


def obtener_red_y_mascara(direccion_ip):
    """
    Calcula la dirección de red y la máscara de red para una dirección IP dada.
    """
    octetos = direccion_ip.split(".")
    binarios = [bin(int(octeto))[2:].zfill(8) for octeto in octetos]
    binario = "".join(binarios)
    num_unos = len(re.match(r"^(1+)", binario).group(1))
    mascara_red_bin = "1" * num_unos + "0" * (32 - num_unos)
    mascara_red_octetos = [int(mascara_red_bin[i:i+8], 2) for i in range(0, 32, 8)]
    mascara_red = ".".join(str(octeto) for octeto in mascara_red_octetos)
    direccion_red_octetos = [int(binarios[i], 2) & int(mascara_red_octetos[i]) for i in range(4)]
    direccion_red = ".".join(str(octeto) for octeto in direccion_red_octetos)
    return direccion_red, mascara_red


def obtener_num_bits_subredes(num_subredes):
    """
    Calcula la cantidad de bits necesarios para la cantidad de subredes especificada.
    """
    return len(bin(num_subredes - 1)) - 2


def obtener_num_bits_hosts(max_host):
    """
    Calcula la cantidad de bits necesarios para la cantidad máxima de hosts especificada.
    """
    return len(bin(max_host + 1)) - 2


def obtener_subred_actual(direccion_red, mascara_red):
    """
    Calcula la dirección de subred actual para una dirección de red y una máscara de red dadas.
    """
    octetos_red = direccion_red.split(".")
    octetos_mascara = mascara_red.split(".")
    subred_actual = [int(octetos_red[i]) & int(octetos_mascara[i]) for i in range(4)]
    return subred_actual


def obtener_num_bits_mascara(mascara_red):
    """
    Calcula el número de bits de la máscara de red.
    """
    num_bits = 0
    for octeto in mascara_red.split('.'):
        num_bits += bin(int(octeto)).count('1')
    return num_bits


def calcular_salto_subred(num_bits_salto):
    """
    Calcula el salto para las subredes.
    """
    return 2 ** num_bits_salto


def list_to_ip(direccion):
    """
    Convierte una lista de números en una dirección IP en formato string.
    """
    return '.'.join(str(octeto) for octeto in direccion)

def subnetting(direccion_ip, num_subredes, max_host):
    """
    Realiza el cálculo de subnetting para una dirección IP dada y una cantidad de subredes y de hosts por subred.
    Devuelve una lista de tuplas, donde cada tupla contiene la dirección de subred, la dirección de broadcast y el rango
    de direcciones de host para cada subred.
    """
    # Verificar si la dirección IP es válida
    if not verificar_direccion_ip(direccion_ip):
        print("Error: La dirección IP es inválida.")
        return

    # Obtener la dirección de red y la máscara de red
    direccion_red, mascara_red = obtener_red_y_mascara(direccion_ip)

    # Obtener la cantidad de bits para subredes y hosts
    num_bits_subredes = obtener_num_bits_subredes(num_subredes)
    num_bits_hosts = obtener_num_bits_hosts(max_host)

    # Verificar si la máscara de red tiene suficientes bits para subredes y hosts
    if not verificar_direccion_ip(mascara_red, num_bits_subredes=num_bits_subredes, num_bits_hosts=num_bits_hosts):
        print("Error: La máscara de red no tiene suficientes bits para la cantidad de subredes y hosts especificados.")
        return

    # Obtener la dirección de subred actual y calcular el salto para las subredes
    subred_actual = obtener_subred_actual(direccion_red, mascara_red)
    num_bits_mascara = obtener_num_bits_mascara(mascara_red)
    num_bits_salto = num_bits_mascara - num_bits_subredes - num_bits_hosts
    salto_subred = calcular_salto_subred(num_bits_salto)

    # Calcular los rangos de direcciones de host para cada subred
    rangos = []
    for i in range(num_subredes):
        # Obtener la dirección de la subred
        subred = subred_actual.copy()
        subred[-1] += i * salto_subred

        # Obtener la dirección de broadcast
        broadcast = subred.copy()
        broadcast[-1] += salto_subred - 1

        # Calcular el rango de direcciones de host para la subred
        primer_host = subred.copy()
        primer_host[-1] += 1
        ultimo_host = broadcast.copy()
        ultimo_host[-1] -= 1

        # Agregar el rango de direcciones a la lista
        rangos.append((list_to_ip(primer_host), list_to_ip(ultimo_host)))

        # Imprimir la información de la subred
        print(f"Subred {i+1}:            {list_to_ip(subred)}")
        print(f"Dirección del primer host: {list_to_ip(primer_host)}")
        print(f"Dirección del último host: {list_to_ip(ultimo_host)}")
        print(f"Broadcast {i+1}:         {list_to_ip(broadcast)}\n")

    return rangos 
subnetting("192.168.1.0",2,10)
